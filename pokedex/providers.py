from fastapi import Depends

from pokedex.common.database.unit_of_work import DatabaseUnitOfWork
from pokedex.common.dependencies import get_db, get_settings
from pokedex.config import Settings
from pokedex.healthcheck.service import HealthCheckService


def get_healthcheck_service(
    config: Settings = Depends(get_settings), db: "DatabaseUnitOfWork" = Depends(get_db)
) -> HealthCheckService:
    return HealthCheckService(settings=config, db=db)
