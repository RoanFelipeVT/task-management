from uuid import UUID
from datetime import datetime, date
from typing import Optional
from pydantic import BaseModel, EmailStr, ConfigDict, Field, field_validator
from .validators import *



class UserBase(BaseModel):
    email: EmailStr = Field(..., max_length=255)
    username: str = Field(..., min_length=3, max_length=50)
    cellphone: str = Field(..., pattern=r"^\+?1?\d{9,15}", max_length=20)
    birth_date: date = Field(..., lt=date.today(), gt=MIN_BIRTH_DATE)

class UserCreate(UserBase):
    password: str = Field(..., min_length=8)

    @field_validator('password')
    @classmethod
    def validate_password_complexity(cls, v):
        return validate_password(v)



class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    username: Optional[str] = Field(None, min_length=3, max_length=50)
    password: Optional[str] = Field(None, min_length=8, max_length=128)

    @field_validator('password')
    @classmethod
    def validate_password_complexity(cls, v):
        return validate_password(v)


class UserResponse(UserBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

