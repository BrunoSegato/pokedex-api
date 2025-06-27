from pokedex.healthcheck.docs.examples import (
    get_healthcheck_available_example,
    get_healthcheck_unavailable_example,
    get_ping_available_example,
)
from pokedex.healthcheck.schemas import HealthCheckModel, PingModel

healthcheck_responses = {
    200: {
        "model": HealthCheckModel,
        "description": "Service is healthy",
        "content": {
            "application/json": {"example": get_healthcheck_available_example()}
        },
    },
    503: {
        "model": HealthCheckModel,
        "description": "Service is unhealthy",
        "content": {
            "application/json": {"example": get_healthcheck_unavailable_example()}
        },
    },
}
ping_responses = {
    200: {
        "model": PingModel,
        "description": "Service is healthy",
        "content": {"application/json": {"example": get_ping_available_example()}},
    },
}
