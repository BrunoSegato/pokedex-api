import pytest

from pokedex.app import Application
from pokedex.config import Settings, get_settings
from tests.fake.routers import routers


@pytest.fixture(scope="function")
def routes() -> list:
    return routers


@pytest.fixture(scope="function")
def application(routes) -> Application:
    return Application(routes)


@pytest.fixture
def settings() -> Settings:
    return get_settings()
