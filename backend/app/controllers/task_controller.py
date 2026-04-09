from typing import List

from fastapi import APIRouter, Depends

from app.core.security import get_current_user
from app.models import User
from app.dto.input.task import TaskCreate, TaskUpdate
from app.dto.output.task import TaskResponse
from app.services.task_service import TaskService

router = APIRouter()


@router.get("/", response_model=List[TaskResponse])
async def list_tasks(user: User = Depends(get_current_user)):
    return await TaskService.list_tasks(user.id)


@router.post("/", response_model=TaskResponse, status_code=201)
async def create_task(data: TaskCreate, user: User = Depends(get_current_user)):
    return await TaskService.create_task(data, user.id)


@router.patch("/{task_id}", response_model=TaskResponse)
async def update_task(task_id: int, data: TaskUpdate, user: User = Depends(get_current_user)):
    return await TaskService.update_task(task_id, data, user.id)


@router.delete("/{task_id}")
async def delete_task(task_id: int, user: User = Depends(get_current_user)):
    return await TaskService.delete_task(task_id, user.id)
