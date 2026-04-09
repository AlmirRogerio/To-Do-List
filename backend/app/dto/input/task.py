from pydantic import BaseModel, Field, field_validator


class TaskCreate(BaseModel):
    name: str = Field(..., min_length=1)
    description: str = Field("", max_length=1000)

    @field_validator("name")
    @classmethod
    def name_must_not_be_blank(cls, v: str) -> str:
        stripped = v.strip()
        if not stripped:
            raise ValueError("name must not be blank or whitespace-only")
        return stripped


class TaskUpdate(BaseModel):
    completed: bool | None = None
    name: str | None = Field(None, min_length=1)
    description: str | None = Field(None, max_length=1000)

    @field_validator("name")
    @classmethod
    def name_must_not_be_blank(cls, v: str | None) -> str | None:
        if v is None:
            return v
        stripped = v.strip()
        if not stripped:
            raise ValueError("name must not be blank or whitespace-only")
        return stripped
