from pokedex.app import Application


class TestApplication:

    def test_check_instance(self, application):
        assert isinstance(application, Application)
