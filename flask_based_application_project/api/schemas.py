from typing import List

from pydantic import BaseModel




class UserBase(BaseModel):
    email_id: str
    username: str

class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    # is_active: bool
    # items: List[Item] = []

    class Config:
        orm_mode = True