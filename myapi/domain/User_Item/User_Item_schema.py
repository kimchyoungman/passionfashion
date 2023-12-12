from pydantic import BaseModel


class User_Item(BaseModel):
    id: int
    User_id: int
    Product_id: int


    class Config:
        orm_mode = True