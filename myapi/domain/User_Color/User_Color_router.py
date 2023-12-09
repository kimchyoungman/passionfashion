from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from domain.User_Color import User_Color_schema
from models import User_Color  # Correct import for the User_Color model

router = APIRouter(
    prefix="/api/User_Color",
)


@router.get("/list", response_model=list[User_Color_schema.User_Color])
def User_Color_list(db: Session = Depends(get_db)):
    _user_color_list = db.query(User_Color).all()  # Corrected usage of User_Color model
    db.close()
    return _user_color_list
