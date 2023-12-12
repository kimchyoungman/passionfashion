from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database import Base

class User_Profile(Base):
    __tablename__ = "User_Profile"
    User_id = Column(Integer, primary_key=True)
    name = Column(String(100))
    sex = Column(String(100))
    age = Column(Integer)

    user_item = relationship("User_Item", back_populates="user_profile")

class User_Item(Base):
    __tablename__ = "User_Item"

    id = Column(Integer, primary_key=True)
    User_id = Column(Integer, ForeignKey("User_Profile.User_id"))
    Product_id = Column(Integer, ForeignKey("Item.Product_id"))

    user_profile = relationship("User_Profile", back_populates="user_item")
    item = relationship("Item", back_populates="user_items")

class Item(Base):
    __tablename__ = "Item"
    Product_id = Column(Integer, primary_key=True)
    Product_name = Column(String(100), nullable=False)
    Product_url = Column(String(100), nullable=False)
    Image_url = Column(String(100), nullable=False)
    Brand = Column(String(100), nullable=False)
    Style = Column(String(100), nullable=False)

    detailed_item = relationship('Detailed_Item', back_populates='item', uselist=False)
    user_items = relationship("User_Item", back_populates="item")

class Detailed_Item(Base):
    __tablename__ = "Detailed_Item"
    Product_id = Column(Integer, ForeignKey("Item.Product_id"), primary_key=True, unique=True)
    Price = Column(Integer, nullable=False)
    Review = Column(Integer, nullable=False)
    Like = Column(Integer, nullable=False)
    Category = Column(String(100), nullable=False)

    item = relationship("Item", back_populates="detailed_item")
