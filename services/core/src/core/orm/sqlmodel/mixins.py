from datetime import datetime
from uuid import UUID, uuid4

from sqlmodel import Field, SQLModel


class TimestampMixin(SQLModel):
    created_at: datetime | None = Field(default=datetime.now(), nullable=False)
    updated_at: datetime | None = Field(default_factory=datetime.now, nullable=False)


class SoftDeleteMixin(SQLModel):
    deleted_at: datetime | None = Field(default=None, nullable=True)


class UUIDMixin(SQLModel):
    id: UUID | None = Field(
        default_factory=uuid4,
        primary_key=True,
    )


__all__ = ["TimestampMixin", "UUIDMixin", "SoftDeleteMixin"]
