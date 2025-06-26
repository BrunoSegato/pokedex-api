from pokedex.app import Application
from pokedex.main import app


class TestMain:

    def test_app_instance(self):
        assert isinstance(app, Application)
