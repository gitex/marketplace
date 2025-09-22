from uuid import UUID

from core.mixins.models import TimeStampMixin, UUIDMixin
from sqlmodel import Column, Enum, Field, SQLModel

from src.constants import AddressKind, Role

#
# class TimeStampMixin(SQLModel):
#     created_at: datetime = Field(default=datetime.now(), nullable=False)
#     updated_at: datetime | None = Field(default_factory=datetime.now, nullable=False)
#
#
# class UUIDMixin(SQLModel):
#     id: UUID | None = Field(
#         default_factory=uuid4,
#         primary_key=True,
#     )
#


class User(UUIDMixin, TimeStampMixin, SQLModel, table=True):
    email: str
    username: str
    phone: str | None = None
    role: Role = Field(default=Role.USER, sa_column=Column(Enum(Role)))
    is_active: bool = True
    is_email_verified: bool = False


class Address(UUIDMixin, TimeStampMixin, SQLModel, table=True):
    user_id: UUID = Field(foreign_key="user.id")
    kind: AddressKind = Field(sa_column=Column(Enum(AddressKind)))
    country: str
    city: str
    postal_code: str
    line1: str
    line2: str
    is_primary: bool = False
