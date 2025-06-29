from contextlib import asynccontextmanager

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from pokedex.config import Settings


class DatabaseUnitOfWork:

    def __init__(self, settings: Settings) -> None:
        self._engine = create_async_engine(
            settings.postgres_url,
            echo=False,
            future=True,
        )
        self._session_factory = async_sessionmaker(
            bind=self._engine,
            expire_on_commit=False,
        )
        self.session: AsyncSession

    @asynccontextmanager
    async def __call__(self):
        async with self._session_factory() as session:
            self.session = session
            try:
                yield self
                await session.commit()
            except Exception:
                await session.rollback()
                raise
            finally:
                await session.close()

    def execute_query(self, query: str):
        return text(query)
