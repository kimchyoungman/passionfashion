from sqlalchemy import func
from sqlalchemy.orm import Session
from fastapi import HTTPException
from models import User_Item

from domain.User_Item import User_Item_schema


def create_user_item(db: Session, user_item: User_Item_schema.User_Item):
    db_user_item = user_item
    db.add(db_user_item)
    db.commit()
    db.refresh(db_user_item)
    return db_user_item


def get_user_item(db: Session):
    random_user_items = db.query(User_Item).order_by(func.random()).limit(1).all()
    if random_user_items:
        return random_user_items
    raise HTTPException(status_code=404, detail="User_Items not found")
