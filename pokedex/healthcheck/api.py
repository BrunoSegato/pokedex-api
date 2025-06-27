from fastapi import APIRouter, Depends, Response, status

from pokedex.healthcheck.docs.responses import healthcheck_responses, ping_responses
from pokedex.healthcheck.schemas import HealthCheckModel, PingModel
from pokedex.healthcheck.service import HealthCheckService
from pokedex.providers import get_healthcheck_service

router = APIRouter(tags=["Health"])


@router.get(
    "/healthcheck",
    response_model=HealthCheckModel,
    summary="Check the overall health of the service",
    responses=healthcheck_responses,
    response_model_exclude_none=True,
)
async def healthcheck(
    response: Response, service: HealthCheckService = Depends(get_healthcheck_service)
):
    result, status_code = await service.is_healthy()
    response.status_code = status_code
    return result


@router.get(
    "/ping",
    response_model=PingModel,
    summary="Check if the service is responsive",
    status_code=status.HTTP_200_OK,
    responses=ping_responses,
)
async def ping(service: HealthCheckService = Depends(get_healthcheck_service)):
    return service.ping()
