from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from pokedex.common.dependencies import get_settings
from pokedex.common.logs.config import config_logging
from pokedex.utils import load_identifier

settings = get_settings()


class Application(FastAPI):
    def __init__(self: "Application", routers: list, middlewares: list):
        super().__init__(
            title=settings.app_name,
            version=settings.version,
            default_response_class=ORJSONResponse,
        )
        config_logging(settings)
        self._load_middlewares(middlewares)
        self._load_routers(routers)

    def _load_routers(self, routers: list):
        for name in routers:
            router = load_identifier(name)
            self.include_router(router)

    def _load_middlewares(self, middlewares: list):
        for name in middlewares:
            middleware = load_identifier(name)
            self.add_middleware(middleware)
