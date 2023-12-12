from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from domain.User_Profile import User_Profile_schema, User_Profile_crud

router = APIRouter(
    prefix="/api/user_profile",
)


@router.post("/", response_model=User_Profile_schema.User_Profile)
def create_user_profile(user_profile: User_Profile_schema.User_Profile, db: Session = Depends(get_db)):
    return User_Profile_crud.create_user_profile(db=db, profile=user_profile)


@router.get("/", response_model=List[User_Profile_schema.User_Profile])
def get_user_profile(db: Session = Depends(get_db)):
    return User_Profile_crud.get_user_profile(db)
