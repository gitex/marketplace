try:
    from pydantic import BaseModel, Field
except ImportError as e:
    raise RuntimeError("Install core[pydantic] to use FastAPI pagination") from e


LIMIT_DESCRIPTION = "Количество элементов на одной странице"
OFFSET_DESCRIPTION = "Количество элементов, которые пропускаем"


class PageParams(BaseModel):
    limit: int = Field(
        ge=1,
        le=100,
        default=10,
        description=LIMIT_DESCRIPTION,
    )
    offset: int = Field(
        ge=0,
        default=0,
        description=OFFSET_DESCRIPTION,
    )


class Page[T](BaseModel):
    total: int = Field(ge=0, description="Общее количество элементов")
    limit: int = Field(ge=1, le=100, description=LIMIT_DESCRIPTION)
    offset: int = Field(ge=0, description=OFFSET_DESCRIPTION)
    items: list[T] = Field(default_factory=list, description="Список элементов")
