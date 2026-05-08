from typing import List

from app.models import Task


class TaskRepository:

    @staticmethod
    async def find_all_by_user(user_id: int) -> List[Task]:
        return await Task.filter(user_id=user_id).all()

    @staticmethod
    async def find_by_id_and_user(task_id: int, user_id: int) -> Task | None:
        return await Task.get_or_none(id=task_id, user_id=user_id)

    @staticmethod
    async def create(name: str, description: str, user_id: int) -> Task:
        return await Task.create(name=name, description=description, user_id=user_id)

    @staticmethod
    async def update(task: Task, **fields) -> Task:
        for key, value in fields.items():
            if value is not None:
                setattr(task, key, value)
        await task.save()
        return task

    @staticmethod
    async def delete(task: Task) -> None:
        await task.delete()
