from typing import List

from fastapi import HTTPException

from app.models import Task
from app.repositories.task_repository import TaskRepository
from app.dto.input.task import TaskCreate, TaskUpdate


class TaskService:

    @staticmethod
    async def list_tasks(user_id: int) -> List[Task]:
        return await TaskRepository.find_all_by_user(user_id)

    @staticmethod
    async def create_task(data: TaskCreate, user_id: int) -> Task:
        return await TaskRepository.create(
            name=data.name,
            description=data.description,
            user_id=user_id,
        )

    @staticmethod
    async def update_task(task_id: int, data: TaskUpdate, user_id: int) -> Task:
        if not (task := await TaskRepository.find_by_id_and_user(task_id, user_id)):
            raise HTTPException(status_code=404, detail="Tarefa não encontrada")

        return await TaskRepository.update(
            task,
            completed=data.completed,
            name=data.name,
            description=data.description,
        )

    @staticmethod
    async def delete_task(task_id: int, user_id: int) -> dict:
        if not (task := await TaskRepository.find_by_id_and_user(task_id, user_id)):
            raise HTTPException(status_code=404, detail="Tarefa não encontrada")

        await TaskRepository.delete(task)
        return {"message": "Tarefa deletada com sucesso"}
