import logging
from functools import lru_cache

from pydantic import KafkaDsn, PostgresDsn, RedisDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Users"
    debug: bool = False
    port: int = 8000
    log_level: str = logging.getLevelName(logging.INFO)
    reload: bool = False
    workers: int = 1
    postgres_dsn: PostgresDsn | None = None
    postgres_echo: bool = False
    redis_dsn: RedisDsn | None = None
    kafka_broker: KafkaDsn | None = None

    model_config = SettingsConfigDict(
        validate_default=True, env_file=(".env",), extra="ignore"
    )


@lru_cache(maxsize=None)
def get_settings() -> Settings:
    return Settings()


settings: Settings = get_settings()
