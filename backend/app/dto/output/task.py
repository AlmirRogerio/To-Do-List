from pydantic import BaseModel


class TaskResponse(BaseModel):
    id: int
    name: str
    description: str
    completed: bool

    class Config:
        from_attributes = True
