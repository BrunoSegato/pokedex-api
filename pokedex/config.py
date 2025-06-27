from functools import lru_cache
from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = Field(
        default="pokedex-api",
        description="Nome da aplicação (exibido em logs, healthcheck etc)",
    )
    environment: str = Field(
        default="development",
        description="Ambiente de execução (development, staging, production)",
    )
    version: str = Field(default="0.0.1", description="Versão atual da aplicação")

    log_level: str = Field(default="INFO", description="Level dos logs do serviço")
    log_formatter: Literal["standard", "json"] = Field(
        default="standard", description="Tipo de formato dos logs do serviço"
    )

    model_config = SettingsConfigDict(
        env_file=".env", env_file_enconding="utf-8", case_sensitive=False
    )


@lru_cache()
def get_settings() -> Settings:
    return Settings()
