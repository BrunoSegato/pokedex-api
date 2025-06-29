from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from pokedex.common.database.base import Base


class Pokemon(Base):
    __tablename__ = "pokemons"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    number: Mapped[int] = mapped_column(Integer)
