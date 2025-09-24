from typing import Annotated

from fastapi import Depends
from sqlmodel import Session

from src.database import get_session
from src.users.services import UserService


def get_user_service(session: Session = Depends(get_session)):
    return UserService(session)


UserServiceDependency = Annotated[UserService, Depends(get_user_service)]
