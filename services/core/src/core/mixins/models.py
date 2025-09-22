from datetime import datetime
from uuid import UUID, uuid4

try:
    from sqlmodel import Field, SQLModel
except ImportError:
    SQLModel = object  # type: ignore

    def Field(*a, **k):  # type: ignore
        return None


class TimeStampMixin(SQLModel):
    created_at: datetime = Field(default=datetime.now(), nullable=False)
    updated_at: datetime | None = Field(default_factory=datetime.now, nullable=False)


class UUIDMixin(SQLModel):
    id: UUID | None = Field(
        default_factory=uuid4,
        primary_key=True,
    )


__all__ = ["TimeStampMixin", "UUIDMixin"]
