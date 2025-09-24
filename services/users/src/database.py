from typing import Annotated, Generator

from fastapi import Depends
from pydantic_settings import SettingsError
from sqlalchemy import Engine
from sqlmodel import Session, SQLModel, create_engine

from .config import settings


def build_engine() -> Engine:
    postgres_dsn = settings.postgres_dsn

    if not postgres_dsn:
        raise SettingsError("Environment variable POSTGRES_DSN is required.")

    return create_engine(
        postgres_dsn.encoded_string(),
        connect_args={"check_same_thread": False},
        echo=settings.debug,
    )


def init_db() -> None:
    # from .addresses.models import Address  # noqa: F401
    # from .users.models import User  # noqa: F401

    engine = build_engine()

    SQLModel.metadata.create_all(engine)


def get_session() -> Generator[Session, None, None]:
    engine = build_engine()

    with Session(engine) as session:
        yield session


SessionDependency = Annotated[Session, Depends(get_session)]
