from uuid import UUID

from sqlmodel import Session, func, select

from .models import User


class UserService:
    def __init__(self, session: Session):
        self.session = session

    def create(self, user: dict) -> User:
        user_db = User.model_validate(user)

        self.session.add(user_db)
        self.session.commit()
        self.session.refresh(user_db)

        return user_db

    def get(self, user_id: UUID) -> User | None:
        return self.session.get(User, user_id)

    def list(self, *, offset: int = 0, limit: int = 0) -> tuple[list[User], int]:
        items = list(self.session.exec(select(User).offset(offset).limit(limit)).all())
        total = self.session.exec(select(func.count()).select_from(User)).one()

        return items, total

    def delete(self, user_id: UUID) -> bool:
        user = self.get(user_id)

        if user:
            self.session.delete(user)
            self.session.commit()
            return True
        return False
