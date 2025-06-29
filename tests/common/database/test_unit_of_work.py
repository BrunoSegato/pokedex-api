import pytest

from pokedex.common.database.unit_of_work import DatabaseUnitOfWork


class TestDatabaseUnitOfWork:

    def test_check_instance(self, mock_uow):
        uow, mock_session = mock_uow
        assert isinstance(uow, DatabaseUnitOfWork)

    @pytest.mark.asyncio
    async def test_failed_commit(self, mock_uow):
        uow, mock_session = mock_uow
        mock_session.commit.side_effect = Exception("Test Error")

        with pytest.raises(Exception, match="Test Error"):
            async with uow() as unit:
                await unit.session.execute("SELECT 1")

        mock_session.commit.assert_awaited_once()
        mock_session.rollback.assert_awaited_once()
        mock_session.close.assert_awaited_once()
