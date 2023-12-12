from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import func
from typing import List

from database import get_db
from domain.Item import Item_schema, Item_crud
from domain.User_Item import User_Item_schema, User_Item_crud

router = APIRouter(
    prefix="/api/user_item",
)


@router.post("/", response_model=User_Item_schema.User_Item)
def create_item(item: Item_schema.Item, db: Session = Depends(get_db)):
    return Item_crud.create_item(db=db, item=item)


@router.get("/", response_model=List[User_Item_schema.User_Item])
def get_user_items(db: Session = Depends(get_db)):
    return User_Item_crud.get_user_item(db)
