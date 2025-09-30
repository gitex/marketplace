import logging

from pydantic import Field, KafkaDsn, PostgresDsn, RedisDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class Database(BaseSettings):
    model_config = SettingsConfigDict()

    url: PostgresDsn = Field(alias="DATABASE_URL")
    echo: bool = Field(alias="DATABASE_ECHO", default=False)
    connections: int = Field(alias="DATABASE_POOL_SIZE", default=20)


class Settings(BaseSettings):
    name: str = Field(alias="APP_NAME", default="Users")
    debug: bool = Field(alias="DEBUG", default=False)
    log_level: str = Field(
        alias="LOG_LEVEL", default=logging.getLevelName(logging.INFO)
    )
    redis_url: RedisDsn = Field(alias="REDIS_URL")
    kafka_url: KafkaDsn = Field(alias="KAFKA_URL")

    database: Database

    model_config = SettingsConfigDict(
        extra="ignore",
    )


def get_settings() -> Settings:
    return Settings(
        database=Database(),
    )


settings = get_settings()
