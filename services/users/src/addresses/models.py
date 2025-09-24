from uuid import UUID

from core.orm.sqlmodel import TimestampMixin, UUIDMixin
from sqlmodel import Column, Enum, Field, SQLModel

from .constants import AddressKind


class Address(SQLModel, UUIDMixin, TimestampMixin, table=True):  # type: ignore
    user_id: UUID = Field(foreign_key="user.id")
    kind: AddressKind = Field(sa_column=Column(Enum(AddressKind)))
    country: str
    city: str
    postal_code: str
    line1: str = ""
    line2: str = ""
    is_primary: bool = False

    class Meta:
        tablename = "addresses"
