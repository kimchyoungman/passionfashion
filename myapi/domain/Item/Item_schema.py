from pydantic import BaseModel


class Item(BaseModel):
    Product_id: int
    Product_name: str
    Product_url: str
    Image_url: str
    Brand: str
    Style: str
    class Config:
        orm_mode = True


class Inter_Item(BaseModel):
    Product_id: int
    Product_name: str
    Product_url: str
    Image_url: str
    Brand: str
    Style: str
    Price: int
    Review: int
    Like: int
    Category: str

    class Config:
        orm_mode = True