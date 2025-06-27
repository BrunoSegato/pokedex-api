from fastapi import Depends

from pokedex.config import Settings, get_settings
from pokedex.healthcheck.service import HealthCheckService


def get_healthcheck_service(
    settings: Settings = Depends(get_settings),
) -> HealthCheckService:
    return HealthCheckService(settings=settings)
