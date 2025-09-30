import logging

from pydantic import Field, KafkaDsn, PostgresDsn, RedisDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class Database(BaseSettings):
    model_config = SettingsConfigDict()

    url: PostgresDsn = Field(alias="DATABASE_URL")
    echo: bool = Field(alias="DATABASE_ECHO", default=False)
    connections: int = Field(alias="DATABASE_POOL_SIZE", default=20)


class Settings(BaseSettings):
    app_name: str = "Users"
    debug: bool = False
    port: int = 8000
    log_level: str = logging.getLevelName(logging.INFO)
    reload: bool = False
    workers: int = 1
    redis_dsn: RedisDsn | None = None
    kafka_broker: KafkaDsn | None = None

    database: Database

    model_config = SettingsConfigDict(
        extra="ignore",
        env_prefix="",
    )


def get_settings() -> Settings:
    return Settings(
        database=Database(),
    )


settings = get_settings()
