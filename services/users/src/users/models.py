from core.orm.sqlmodel import TimestampMixin, UUIDMixin
from pydantic import EmailStr
from sqlmodel import Column, Enum, Field

from .constants import Role


class User(TimestampMixin, UUIDMixin, table=True):  # type: ignore
    __tablename__ = "users"

    email: EmailStr
    username: str
    phone: str | None = None
    role: Role = Field(default=Role.USER, sa_column=Column(Enum(Role)))
    is_active: bool = True
    is_email_verified: bool = False
