from pydantic import BaseModel


class CheckModel(BaseModel):
    ok: bool
    latency_ms: float
    error: str | None = None


class PingModel(BaseModel):
    service_name: str
    version: str


class HealthCheckModel(PingModel):
    host: str
    uptime: str | None = None
    timestamp: str
    environment: str
    status: bool
    latency_ms: float
    details: dict[str, CheckModel]
