from pydantic import BaseModel


class HealthCheckModel(BaseModel):
    status: bool
    details: dict[str, bool]


class PingModel(BaseModel):
    service_name: str
    version: str
