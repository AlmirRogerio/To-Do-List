from tortoise import fields
from tortoise.models import Model


class Task(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    description = fields.TextField(default="")
    completed = fields.BooleanField(default=False)
    user = fields.ForeignKeyField("models.User", related_name="tasks")

    class Meta:
        table = "tasks"
