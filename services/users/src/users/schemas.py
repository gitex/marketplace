from uuid import UUID

from pydantic import BaseModel, EmailStr, Field

from src.users.constants import Role


class UserCreate(BaseModel):
    email: EmailStr
    username: str = Field(max_length=30)
    role: Role = Role.USER


class UserRead(BaseModel):
    id: UUID
    email: EmailStr
    username: str
    phone: str
    role: Role
    is_active: bool
    is_email_verified: bool
