from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel.ext.asyncio.session import AsyncSession

from .config import settings

# Lazy engine
engine = create_async_engine(
    settings.database.url.encoded_string(),
    echo=settings.database.echo,
    future=True,
    pool_size=settings.database.connections,
)


# async def init_db() -> None:
#     # from .addresses.models import Address  # noqa: F401
#     from .users.models import User  # noqa: F401
#
#     async with engine.begin() as conn:
#         await conn.run_sync(SQLModel.metadata.create_all)


async def get_session():
    async with AsyncSession(engine) as session:
        yield session


SessionDependency = Annotated[AsyncSession, Depends(get_session)]
