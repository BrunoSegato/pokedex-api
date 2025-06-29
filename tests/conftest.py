from unittest.mock import AsyncMock, MagicMock

import pytest

from pokedex.app import Application
from pokedex.common.dependencies import DatabaseUnitOfWork, get_settings
from pokedex.config import Settings
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


@pytest.fixture
def mock_session(mocker):
    session = AsyncMock()
    return session


@pytest.fixture
def mock_uow(mocker, mock_session, settings):
    factory = MagicMock(return_value=mock_session)
    mocker.patch("pokedex.common.database.unit_of_work.create_async_engine")
    mocker.patch(
        "pokedex.common.database.unit_of_work.async_sessionmaker", return_value=factory
    )
    return DatabaseUnitOfWork(settings=settings)
