# Python

from uuid import UUID # Universal User Identification
from datetime import date
from datetime import datetime
from typing import Optional, List

# Pydantic
from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field


# FastAPI
from fastapi import FastAPI
from fastapi import status

app = FastAPI()


# Models

class UserBase(BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr = Field(...)


class UserLogin(BaseModel):
     password: str = Field(
        ...,
        min_length=8, 
        max_length=20
    )


class User(UserBase):
    first_name: str = Field(
        ...,
        min_length=1, 
        max_length=50
        )
    last_name: str = Field(
        ...,
        min_length=1, 
        max_length=50
    )
    birth_date: Optional[date] = Field(default=None)


class Tweet(BaseModel):
    tweet_id: UUID
    content: str = Field(
        ...,
        min_length=1, 
        max_length=250, 
        )
    created_at: datetime = Field(
        default=datetime.now()
    )
    updated_at: Optional[datetime] = Field(default=None)
    by: User = Field(
        ...
    )


# Path operations


@app.get(path="/")
def home():
    return {"Twitter API": "Working!"}


# Users


@app.post(
    path="/signup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Register a user",
    tags=["Users"]
)
def signup():
    pass


@app.get(
    path="/login",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Login a user",
    tags=["Users"]
)
def login():
    pass


@app.get(
    path="/users",
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary="Show all users",
    tags=["Users"]
)
def show_all_users():
    pass


@app.get(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Show a single user",
    tags=["Users"]
)
def show_single_user():
    pass


@app.delete(
    path="/users/{user_id}/delete",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Delete a user",
    tags=["Users"]
)
def delete_a_user():
    pass


@app.put(
    path="/users/{user_id}/update",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Update a user",
    tags=["Users"]
)
def update_a_user():
    pass


# Tweets

