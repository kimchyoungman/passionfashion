from domain.Detailed_Item import Detailed_Item_schema
from models import Detailed_Item
from sqlalchemy.orm import Session
from fastapi import HTTPException
from sqlalchemy.sql.expression import func


def create_detailed_item(db: Session, detailed_item: Detailed_Item_schema.Detailed_Item):
    detailed_item = Detailed_Item(**detailed_item.dict())
    db.add(detailed_item)
    db.commit()
    db.refresh(detailed_item)
    return detailed_item


def get_detailed_item(db: Session):
    return db.query(Detailed_Item).all()

