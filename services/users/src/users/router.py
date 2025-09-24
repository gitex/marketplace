from typing import Annotated
from uuid import UUID

from core.web.fastapi.pagination import Page, PageParams
from fastapi import APIRouter, Depends, HTTPException, Response, status

from src.users.dependencies import UserServiceDependency
from src.users.schemas import UserRead

router = APIRouter(
    prefix="users/",
    tags=["users"],
)


@router.get("/", response_model=Page[UserRead])
async def get_users(
    params: Annotated[PageParams, Depends(PageParams)],
    service: UserServiceDependency,
):
    """
    Получить всех пользователей.
    """
    users, total = service.list(offset=params.offset, limit=params.limit)
    return Page(total=total, items=users, **params.model_dump())


@router.get("/{user_id}", response_model=UserRead)
async def get_user(
    user_id: UUID,
    service: UserServiceDependency,
):
    """Получить пользователя по id."""
    user = service.get(user_id)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Пользователь не найден"
        )

    return user


@router.delete("/{user_id}")
async def delete_user(
    user_id: UUID,
    service: UserServiceDependency,
):
    """Удалить пользователя по id."""

    deleted = service.delete(user_id)

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Пользователь не найден"
        )

    return Response({}, status_code=status.HTTP_204_NO_CONTENT)
