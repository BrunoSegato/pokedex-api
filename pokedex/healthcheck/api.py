from fastapi import APIRouter, Depends, status
from fastapi.responses import ORJSONResponse

from pokedex.healthcheck.schemas import HealthCheckModel, PingModel
from pokedex.healthcheck.service import HealthCheckService
from pokedex.providers import get_healthcheck_service

router = APIRouter(tags=["health"])


@router.get("/healthcheck", response_model=HealthCheckModel)
async def healthcheck(service: "HealthCheckService" = Depends(get_healthcheck_service)):
    result, status_code = await service.is_healthy()
    return ORJSONResponse(content=result, status_code=status_code)


@router.get("/ping", response_model=PingModel, status_code=status.HTTP_200_OK)
async def ping(service: "HealthCheckService" = Depends(get_healthcheck_service)):
    return service.ping()
