
from pydantic import BaseModel


class User_Color(BaseModel):
    id: int
    User_id: str
    Product_id: str
    Black: int
    Blue: int
    Red: int
    Green: int
    Yellow: int
    White: int

    class Config:
        orm_mode = True
