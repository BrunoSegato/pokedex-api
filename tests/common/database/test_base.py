from pokedex.common.database.base import Base


class TestDatabaseBase:

    def test_check_instance(self):
        base = Base()
        assert isinstance(base, Base)
