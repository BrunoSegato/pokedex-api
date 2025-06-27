from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from pokedex.settings import get_settings
from pokedex.utils import load_identifier

settings = get_settings()


class Application(FastAPI):
    def __init__(self: "Application", routers: list):
        super().__init__(
            title=settings.app_name,
            version=settings.version,
            default_response_class=ORJSONResponse,
        )

        self._load_routers(routers)

    def _load_routers(self, routers: list):
        for name in routers:
            router = load_identifier(name)
            self.include_router(router)
