from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = Field(
        default="pokedex-api",
        description="Application name (used in logs, healthcheck, etc.)",
    )
    environment: str = Field(
        default="development",
        description="Execution environment (development, staging, production)",
    )
    version: str = Field(
        default="0.0.1", description="Current version of the application"
    )

    log_level: str = Field(
        default="INFO", description="Logging level of the application"
    )
    log_formatter: Literal["standard"] = Field(
        default="standard", description="Log formatting style (standard)"
    )

    postgres_url: str = Field(
        default="postgresql+asyncpg://postgres:postgres@localhost:5432/pokedex",
        description="Host do banco de dados Postgres",
    )

    model_config = SettingsConfigDict(
        env_file=".env", env_file_enconding="utf-8", case_sensitive=False
    )
