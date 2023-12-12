from pydantic import BaseModel


class Detailed_Item(BaseModel):
    Product_id: int
    Price: int
    Review: int
    Like: int
    Category: str

    class Config:
        orm_mode = True
