from fastapi import Depends

from pokedex.healthcheck.service import HealthCheckService
from pokedex.settings import Settings, get_settings


def get_healthcheck_service(
    settings: Settings = Depends(get_settings),
) -> HealthCheckService:
    return HealthCheckService(settings=settings)
