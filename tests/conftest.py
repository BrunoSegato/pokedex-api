import pytest

from pokedex.app import Application
from pokedex.config import Settings, get_settings
from pokedex.middlewares import middlewares
from tests.fake.routers import routers


@pytest.fixture(scope="function")
def routes() -> list:
    return routers


@pytest.fixture(scope="function")
def middleware() -> list:
    return middlewares


@pytest.fixture(scope="function")
def application(routes, middleware) -> Application:
    return Application(routes, middleware)


@pytest.fixture
def settings() -> Settings:
    return get_settings()
