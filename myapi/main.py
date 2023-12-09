

from fastapi import Depends, FastAPI, HTTPException
from starlette.middleware.cors import CORSMiddleware


from domain.User_Color import User_Color_router

app = FastAPI()

origins = [
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(User_Color_router.router)