import socket
import time
from datetime import datetime, timezone
from typing import Callable

from fastapi import status

from pokedex.healthcheck.schemas import HealthCheckModel, PingModel


class HealthCheckService:

    CHECK_STATUS = True

    def __init__(self):
        self._checks = {}

    def add_checks(self, name: str, func: Callable) -> None:
        self._checks[name] = func

    def ping(self):
        return PingModel(service_name="pokedex-api", version="0.0.1")

    async def check_service(self):
        return self.CHECK_STATUS

    async def is_healthy(self):
        result = {}
        all_ok = True
        timestamp = datetime.now(timezone.utc).isoformat()
        uptime = self._uptime()

        for name, check_fn in self._checks.items():
            start_check = time.perf_counter()
            try:
                ok = await check_fn()
            except Exception:
                ok = False
            latency = round((time.perf_counter() - start_check) * 1000, 2)

            result[name] = {"ok": ok, "latency_ms": latency}
            if not ok:
                all_ok = False
        total_latency = sum(dep["latency_ms"] for dep in result.values())
        status_code_ok = status.HTTP_200_OK
        status_code_nok = status.HTTP_503_SERVICE_UNAVAILABLE
        return HealthCheckModel(
            service_name="pokedex-api",
            version="0.0.1",
            environment="production",
            host=socket.gethostname(),
            timestamp=timestamp,
            uptime=uptime,
            status=all_ok,
            latency_ms=total_latency,
            details=result,
            status_code=(status_code_ok if all_ok else status_code_nok),
        )

    def _uptime(self) -> str | None:
        try:
            with open("/proc/uptime", "r") as f:
                uptime_seconds = float(f.readline().split()[0])
                hours, remainder = divmod(int(uptime_seconds), 3600)
                minutes, seconds = divmod(remainder, 60)
                return f"{hours}h {minutes}m {seconds}s"
        except Exception:
            return None
