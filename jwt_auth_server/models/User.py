from pydantic import BaseModel, Field


class User(BaseModel):
    _id: int
    username: str
    password: str = Field(min_length=4)
