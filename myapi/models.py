from sqlalchemy import Column, Integer, String
from database import Base


class User_Color(Base):
    __tablename__ = "User_Color"

    id = Column(Integer, primary_key=True, autoincrement=True)
    User_id = Column(String(100), nullable=False)
    Product_id = Column(String(100), nullable=False)
    Black = Column(Integer)
    Blue = Column(Integer)
    Red = Column(Integer)
    Green = Column(Integer)
    Yellow = Column(Integer)
    White = Column(Integer)


class User_Style(Base):
    __tablename__ = "User_Style"

    id = Column(Integer, primary_key=True, autoincrement=True)
    User_id = Column(String(100), nullable=False)
    Product_id = Column(String(100), nullable=False)
    Casual = Column(Integer)
    Minimal = Column(Integer)
    Street = Column(Integer)
    Business = Column(Integer)


class Item(Base):
    __tablename__ = "Item"

    Product_id = Column(String(100), primary_key=True)
    Product_name = Column(String(100), nullable=False)
    Sub_categoary = Column(String(100), nullable=False)
    Link = Column(String(100), nullable=False)
    Image_link = Column(String(100), nullable=False)
    Style = Column(String(100), nullable=False)
    Color = Column(String(100), nullable=False)
    Like = Column(String(100), nullable=False)


class Purchase(Base):
    __tablename__ = "Purchase"

    id = Column(Integer, primary_key=True, autoincrement=True)
    Product_id = Column(String(100), nullable=False)
    User_id = Column(String(100), nullable=False)
