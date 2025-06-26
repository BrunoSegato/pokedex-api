from fastapi import APIRouter, status

from pokedex.healthcheck.schemas import PingModel
from pokedex.healthcheck.service import HealthCheckService

router = APIRouter(tags=["health"])
service = HealthCheckService()


@router.get("/healthcheck", status_code=status.HTTP_200_OK)
async def healthcheck():
    return await service.is_healthy()()


@router.get("/ping", response_model=PingModel, status_code=status.HTTP_200_OK)
async def ping():
    return service.ping()
