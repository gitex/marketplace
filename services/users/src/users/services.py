from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import func, select

from .models import User


class UserService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, user: dict) -> User:
        user_db = User.model_validate(user)

        self.session.add(user_db)
        await self.session.commit()
        await self.session.refresh(user_db)

        return user_db

    async def get(self, user_id: UUID) -> User | None:
        result = await self.session.get(User, user_id)
        return result

    async def list(self, *, offset: int = 0, limit: int = 0) -> tuple[list[User], int]:
        items = await self.session.execute(select(User).offset(offset).limit(limit))
        total = await self.session.execute(select(func.count()).select_from(User))

        return list(items.scalars().fetchall()), total.scalars().one()

    async def delete(self, user_id: UUID) -> bool:
        user = self.get(user_id)

        if user:
            await self.session.delete(user)
            await self.session.commit()
            return True
        return False
