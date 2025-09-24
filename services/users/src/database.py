from typing import Annotated, Any, AsyncGenerator

from fastapi import Depends
from pydantic_settings import SettingsError
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine
from sqlmodel import Session, SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession

from .config import settings


async def build_engine() -> AsyncEngine:
    postgres_dsn = settings.postgres_dsn

    if not postgres_dsn:
        raise SettingsError("Environment variable POSTGRES_DSN is required.")

    return create_async_engine(
        postgres_dsn.encoded_string(),
        echo=settings.postgres_echo,
        future=True,
        pool_size=20,
    )


async def init_db() -> None:
    # from .addresses.models import Address  # noqa: F401
    # from .users.models import User  # noqa: F401

    engine = await build_engine()

    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


async def get_session() -> AsyncGenerator[AsyncSession, Any]:
    engine = await build_engine()

    async with AsyncSession(engine) as session:
        yield session


SessionDependency = Annotated[Session, Depends(get_session)]
