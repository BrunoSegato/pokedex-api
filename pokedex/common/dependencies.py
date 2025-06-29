from collections.abc import AsyncGenerator
from functools import lru_cache

from sqlalchemy.ext.asyncio import AsyncSession

from pokedex.common.database.unit_of_work import DatabaseUnitOfWork
from pokedex.config import Settings


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    uow = DatabaseUnitOfWork(settings=get_settings())
    async with uow() as unit:
        yield unit


@lru_cache()
def get_settings() -> Settings:
    return Settings()
