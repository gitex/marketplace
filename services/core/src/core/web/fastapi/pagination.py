from __future__ import annotations

from typing import Annotated, Generic, List, TypeVar

from fastapi import Depends
from pydantic import BaseModel, Field, NonNegativeInt, PositiveInt

T = TypeVar("T")

DEFAULT_LIMIT = 10
DEFAULT_OFFSET = 0

LIMIT_DESCRIPTION = "Количество элементов на одной странице"
OFFSET_DESCRIPTION = "Количество элементов, которые пропускаем"


class PageParams(BaseModel):
    limit: PositiveInt = Field(
        ge=1,
        le=100,
        default=DEFAULT_LIMIT,
        description=LIMIT_DESCRIPTION,
    )
    offset: NonNegativeInt = Field(
        ge=0,
        default=DEFAULT_OFFSET,
        description=OFFSET_DESCRIPTION,
    )


class Page(BaseModel, Generic[T]):
    total: NonNegativeInt = Field(ge=0, description="Общее количество элементов")
    limit: PositiveInt = Field(
        ge=1, le=100, default=DEFAULT_LIMIT, description=LIMIT_DESCRIPTION
    )
    offset: NonNegativeInt = Field(
        ge=0, default=DEFAULT_OFFSET, description=OFFSET_DESCRIPTION
    )
    items: List[T] = Field(default_factory=list, description="Список элементов")


PageParamsDependency = Annotated[PageParams, Depends(PageParams)]
