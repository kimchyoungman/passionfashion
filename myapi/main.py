from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from domain.Detailed_Item import Detailed_Item_router
from domain.Item import Item_router
from domain.User_Item import User_Item_router
from domain.User_Profile import User_Profile_router

app = FastAPI()

origins = [
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(Item_router.router)
app.include_router(User_Item_router.router, tags=["item"])
app.include_router(Detailed_Item_router.router)
app.include_router(User_Profile_router.router)
