import asyncio
from unittest.mock import AsyncMock

import pytest
from alembic import command
from alembic.config import Config

from pokedex.app import Application
from pokedex.common.dependencies import DatabaseUnitOfWork, get_settings
from pokedex.config import Settings
from pokedex.middlewares import middlewares
from tests.fake.routers import routers


@pytest.fixture(scope="session")
def event_loop():
    return asyncio.get_event_loop()


@pytest.fixture(scope="session", autouse=True)
def run_migrations():
    alembic_cfg = Config("alembic.ini")
    alembic_cfg.set_main_option(
        "sqlalchemy.url", get_settings().postgres_url.replace("+asyncpg", "")
    )
    command.upgrade(alembic_cfg, "head")


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
def mock_session_factory(mocker):
    mock_session = AsyncMock()
    mock_session.execute = AsyncMock()
    mock_session.commit = AsyncMock()
    mock_session.rollback = AsyncMock()
    mock_session.close = AsyncMock()

    mock_session_cm = AsyncMock()
    mock_session_cm.__aenter__.return_value = mock_session
    factory = mocker.Mock(return_value=mock_session_cm)

    return factory, mock_session


@pytest.fixture(scope="function")
def mock_uow(mocker, mock_session_factory, settings):
    factory, mock_session = mock_session_factory
    mocker.patch("pokedex.common.database.unit_of_work.create_async_engine")
    mocker.patch(
        "pokedex.common.database.unit_of_work.async_sessionmaker", return_value=factory
    )
    uow = DatabaseUnitOfWork(settings=settings)
    return uow, mock_session
