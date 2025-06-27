from datetime import datetime, timezone

from pokedex.healthcheck.schemas import HealthCheckModel, PingModel


def get_healthcheck_unavailable_example():
    return HealthCheckModel(
        service_name="pokedex-api",
        version="0.0.1",
        host="example-host",
        uptime="0h 0m 10s",
        timestamp=datetime.now(timezone.utc).isoformat(),
        environment="development",
        status=False,
        latency_ms=0.01,
        details={"service": {"ok": False, "latency_ms": 0.01}},
    ).model_dump()


def get_healthcheck_available_example():
    return HealthCheckModel(
        service_name="pokedex-api",
        version="0.0.1",
        host="example-host",
        uptime="0h 0m 10s",
        timestamp=datetime.now(timezone.utc).isoformat(),
        environment="development",
        status=False,
        latency_ms=0.01,
        details={"service": {"ok": True, "latency_ms": 0.01}},
    ).model_dump()


def get_ping_available_example():
    return PingModel(
        service_name="pokedex-api",
        version="0.0.1",
    ).model_dump()
