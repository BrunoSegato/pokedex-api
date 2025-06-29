import socket
import time
from datetime import datetime, timezone
from typing import Callable

from fastapi import status

from pokedex.common.database.unit_of_work import DatabaseUnitOfWork
from pokedex.common.logs.config import get_logger
from pokedex.config import Settings
from pokedex.healthcheck.repository import HealthCheckRepository
from pokedex.healthcheck.schemas import HealthCheckModel, PingModel

logger = get_logger(__name__)


class HealthCheckService:

    CHECK_STATUS = True
    UPTIME_DIR = "/proc/uptime"
    CODE_503 = status.HTTP_503_SERVICE_UNAVAILABLE
    CODE_200 = status.HTTP_200_OK

    def __init__(self, settings: "Settings", db: "DatabaseUnitOfWork"):
        self._checks: dict[str, Callable] = {}
        self._settings: "Settings" = settings
        self._repository: "HealthCheckRepository" = HealthCheckRepository(db)
        self.add_checks("service", self.check_service)
        self.add_checks("database", self.check_db)

    def add_checks(self, name: str, func: Callable) -> None:
        if name not in self._checks:
            self._checks[name] = func

    def ping(self) -> PingModel:
        return PingModel(
            service_name=self._settings.app_name, version=self._settings.version
        )

    async def check_service(self) -> bool:
        return self.CHECK_STATUS

    async def check_db(self) -> bool:
        try:
            await self._repository.check_connection()
            return True
        except Exception:
            return False

    async def is_healthy(self) -> tuple[HealthCheckModel, int]:
        result = {}
        all_ok = True
        timestamp = datetime.now(timezone.utc).isoformat()
        uptime = self._uptime()

        for name, check_fn in self._checks.items():
            start_check = time.perf_counter()
            error = None
            try:
                ok = await check_fn()
            except Exception as exc:
                ok = False
                error = str(exc)
            latency = round((time.perf_counter() - start_check) * 1000, 2)

            result[name] = {
                "ok": ok,
                "latency_ms": latency,
                **({"error": error} if error else {}),
            }
            if not ok:
                all_ok = False
        total_latency = sum(dep["latency_ms"] for dep in result.values())
        data = {
            "service_name": self._settings.app_name,
            "version": self._settings.version,
            "environment": self._settings.environment,
            "host": socket.gethostname(),
            "timestamp": timestamp,
            "uptime": uptime,
            "status": all_ok,
            "latency_ms": total_latency,
            "details": result,
        }
        status_code = self.CODE_200 if all_ok else self.CODE_503
        model = HealthCheckModel(**data).model_dump(exclude_none=True)
        return model, status_code

    def _uptime(self) -> str | None:
        try:
            with open(self.UPTIME_DIR, "r") as f:
                uptime_seconds = float(f.readline().split()[0])
                hours, remainder = divmod(int(uptime_seconds), 3600)
                minutes, seconds = divmod(remainder, 60)
                return f"{hours}h {minutes}m {seconds}s"
        except Exception:
            return None
