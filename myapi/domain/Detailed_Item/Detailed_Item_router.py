from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import func
from typing import List

from database import get_db
from domain.Detailed_Item import Detailed_Item_crud, Detailed_Item_schema

router = APIRouter(
    prefix="/api/detailed_item",
)


@router.post("/", response_model=Detailed_Item_schema.Detailed_Item)
def create_detailed_item(detailed_item: Detailed_Item_schema.Detailed_Item, db: Session = Depends(get_db)):
    return Detailed_Item_crud.create_detailed_item(db=db, item=detailed_item)


@router.get("/list", response_model=list[Detailed_Item_schema.Detailed_Item])
def item_list(db: Session = Depends(get_db)):
    return Detailed_Item_crud.get_detailed_item(db)
