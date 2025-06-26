import pytest

from pokedex.app import Application
from tests.fake.routers import routers


@pytest.fixture
def routes():
    yield routers


@pytest.fixture
def application(routes):
    yield Application(routes)
