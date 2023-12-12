from pydantic import BaseModel


class User_Profile(BaseModel):
    User_id: int
    name: str
    sex: str
    age: int

    class Config:
        orm_mode = True