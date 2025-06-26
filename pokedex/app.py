from fastapi import FastAPI

from pokedex.utils import load_identifier


class Application(FastAPI):
    def __init__(self: "Application", routers: list):
        super().__init__(title="pokedex-api", version="0.0.1")

        self._load_routers(routers)

    def _load_routers(self, routers: list):
        for name in routers:
            router = load_identifier(name)
            self.include_router(router)
