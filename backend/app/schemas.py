
from datetime import date, datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict, EmailStr, Field


# User schemas
class UserCreate(BaseModel):
    email: EmailStr
    first_name: str = Field(min_length=1, max_length=100)
    last_name: str = Field(min_length=1, max_length=100)
    user_name: str = Field(min_length=1, max_length=50)
    phone_number: str | None = Field(default=None, max_length=20)
    is_active: bool = True
    gender: Literal[
        "male", "female", "other", "prefer_not_to_say"
    ] | None = None
    date_of_birth: date | None = None


class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    user_id: int
    email: str
    first_name: str
    last_name: str
    user_name: str
    phone_number: str | None
    is_active: bool
    gender: str | None
    date_of_birth: date | None


# Task schemas
class TaskCreate(BaseModel):
    user_id: int = Field(gt=0)
    title: str = Field(min_length=1, max_length=200)
    description: str | None = None
    status: Literal["pending", "in_progress", "completed"] = "pending"


class TaskUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=200)
    description: str | None = None
    status: Literal["pending", "in_progress", "completed"] | None = None


class TaskResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    task_id: int
    user_id: int
    title: str
    description: str | None
    status: str
    created_at: datetime
    updated_at: datetime

class UserCreate(BaseModel):
    email:EmailStr
    password: str = Field(min_length=8, max_length=128)
    first_name: str = Field(min_length=1,max_length=100)
    last_name: str = Field(min_length=1, max_length=100)
    user_name: str = Field(min_length=1, max_length=50)
    phone_number: str | None = Field(default=None, max_length=20)
    gender: Literal["male", "female", "other", "prefer_not_to_say"] | None = None
    date_of_birth: date | None = None


class UserLogin(BaseModel):
    email: EmailStr
    password: str = Field(min_length=1, max_length=128)

