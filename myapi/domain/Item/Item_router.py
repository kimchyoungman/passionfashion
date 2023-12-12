from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Item
from models import Detailed_Item
from domain.Item import Item_schema,Item_crud

router = APIRouter(
    prefix="/api/item",
)


@router.post("/", response_model=Item_schema.Item)
def create_item_route(item: Item_schema.Item, db: Session = Depends(get_db)):
    return Item_crud.create_item(db=db, item=item)


@router.get("/random_items", response_model=list[Item_schema.Item])
def get_random_items_route(db: Session = Depends(get_db)):
    return Item_crud.get_random_items(db=db)

@router.get("/style/{style}", response_model=list[Item_schema.Item])
def get_items_by_style(style: str, db: Session = Depends(get_db)):
    return Item_crud.get_items_by_style(db=db, style=style)

@router.get("/user/{user_id}", response_model=list[Item_schema.Item])
def get_items_by_user_id_route(user_id: int, db: Session = Depends(get_db)):
    return Item_crud.get_items_by_user_id(db=db, user_id=user_id)

@router.get("/productid/{product_id}", response_model=Item_schema.Inter_Item)
def get_item_and_detailed_item_by_id(product_id: int, db: Session = Depends(get_db)):
    return Item_crud.get_item_and_detailed_item_by_id(db=db, product_id=product_id)

