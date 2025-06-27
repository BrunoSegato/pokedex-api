from pokedex.common.context import manager


class TestContextManager:

    def test_get_context_manager_by_default(self):
        result = manager.get_context("teste", "default_value")
        assert result == "default_value"

    def test_set_and_get_context_manager(self):
        manager.set_context("field", "value")
        manager.set_context("field_2", "value2")
        assert manager.get_context("field") == "value"
        assert manager.get_context("field_2") == "value2"
