from domain.User_Profile import User_Profile_schema
from models import User_Profile
from sqlalchemy.orm import Session
from fastapi import HTTPException
from sqlalchemy.sql.expression import func


def create_user_profile(db: Session, profile: User_Profile_schema.User_Profile):
    db_profile = profile
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return db_profile


def get_user_profile(db: Session):
    random_user_profile = db.query(User_Profile).order_by(func.random()).limit(1).all()
    if random_user_profile:
        return random_user_profile
    raise HTTPException(status_code=404, detail="User_Profile not found")

