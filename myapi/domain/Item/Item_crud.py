from models import Item, User_Item, Detailed_Item
from sqlalchemy.orm import Session
from domain.Item import Item_schema
from fastapi import HTTPException
from sqlalchemy.sql.expression import func


def create_item(db: Session, item: Item_schema.Item):
    db_item = Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_items_by_user_id(db: Session, user_id: int):
    user_items = db.query(User_Item).filter(User_Item.User_id == user_id).all()
    if not user_items:
        raise HTTPException(status_code=404, detail=f"User with ID {user_id} not found or has no items")

    item_ids = [user_item.Product_id for user_item in user_items]

    items = db.query(Item).filter(Item.Product_id.in_(item_ids)).all()

    return items


def get_random_items(db: Session):
    random_items = db.query(Item).order_by(func.random()).limit(3).all()
    if not random_items:
        raise HTTPException(status_code=404, detail="Items not found")
    return random_items


def get_items_by_style(db: Session, style: str):
    style_items = db.query(Item).filter(Item.Style == style).order_by(func.random()).limit(10).all()

    if not style_items:
        raise HTTPException(status_code=404, detail="not found or has no items")
    return style_items


def get_item_and_detailed_item_by_id(db: Session, product_id: int):
    # Item 테이블의 필드 가져오기
    item_fields = db.query(Item).filter(Item.Product_id == product_id).first()

    if not item_fields:
        return None

    # Detailed_Item 테이블의 필드 가져오기
    detailed_item_fields = (
        db.query(Detailed_Item)
        .filter(Detailed_Item.Product_id == product_id)
        .first()
    )

    if not detailed_item_fields:
        return None

    # 두 필드를 합쳐서 딕셔너리로 반환
    result = {
        "Product_id": item_fields.Product_id,
        "Product_name": item_fields.Product_name,
        "Product_url": item_fields.Product_url,
        "Image_url": item_fields.Image_url,
        "Brand": item_fields.Brand,
        "Style": item_fields.Style,
        "Price": detailed_item_fields.Price,
        "Review": detailed_item_fields.Review,
        "Like": detailed_item_fields.Like,
        "Category": detailed_item_fields.Category,
    }

    return result
