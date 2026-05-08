from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise

from app.controllers import router
from app.core.config import CORS_ORIGINS, DATABASE_URL

app = FastAPI(title="Modern To-do List API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

register_tortoise(
    app,
    db_url=DATABASE_URL,
    modules={"models": ["app.models.user", "app.models.task"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
