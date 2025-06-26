import pytest
from fastapi import APIRouter

from pokedex.utils import load_identifier


class TestLoadIdentifier:

    def test_load_identifier_invalid_name(self):
        with pytest.raises(AttributeError) as exc:
            load_identifier("invalid_name")

        assert str(exc.value) == "Invalid identifier [invalid_name]"

    def test_load_identifier_module_not_found(self):
        with pytest.raises(AttributeError) as exc:
            load_identifier("pokedex.invalid_route.router")

        expected = "Module not found No module named 'pokedex.invalid_route'"
        assert str(exc.value) == expected

    def test_load_identifier(self, routes):
        module = load_identifier(routes[0])
        assert isinstance(module, APIRouter)
