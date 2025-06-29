from pokedex.common.database.unit_of_work import DatabaseUnitOfWork


class HealthCheckRepository:

    def __init__(self, db: "DatabaseUnitOfWork"):
        self._db = db

    async def check_connection(self) -> bool:
        try:
            await self._db.session.execute(self._db.execute_query("SELECT 1"))
            return True
        except Exception:
            return False
