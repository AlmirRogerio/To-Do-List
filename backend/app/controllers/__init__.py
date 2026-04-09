from fastapi import APIRouter

from app.controllers.auth_controller import router as auth_router
from app.controllers.task_controller import router as tasks_router

router = APIRouter()
router.include_router(auth_router, prefix="/auth", tags=["auth"])
router.include_router(tasks_router, prefix="/tasks", tags=["tasks"])
