from unittest.mock import AsyncMock

import pytest

from pokedex.common.database.unit_of_work import DatabaseUnitOfWork


class TestDatabaseUnitOfWork:

    def test_check_instance(self, mock_uow):
        assert isinstance(mock_uow, DatabaseUnitOfWork)

    @pytest.mark.asyncio
    async def test_failed_commit(self, mocker, settings):
        mock_session = AsyncMock()
        mock_session.execute = AsyncMock()
        mock_session.commit = AsyncMock(side_effect=Exception("Test Error"))
        mock_session.rollback = AsyncMock()
        mock_session.close = AsyncMock()

        mock_session_cm = AsyncMock()
        mock_session_cm.__aenter__.return_value = mock_session
        mock_session_factory = mocker.Mock(return_value=mock_session_cm)

        mocker.patch("pokedex.common.database.unit_of_work.create_async_engine")
        mocker.patch(
            "pokedex.common.database.unit_of_work.async_sessionmaker",
            return_value=mock_session_factory,
        )

        uow = DatabaseUnitOfWork(settings)

        with pytest.raises(Exception, match="Test Error"):
            async with uow() as unit:
                await unit.session.execute("SELECT 1")

        mock_session.commit.assert_awaited_once()
        mock_session.rollback.assert_awaited_once()
        mock_session.close.assert_awaited_once()
