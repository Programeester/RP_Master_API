from tortoise import Tortoise, fields, run_async
from tortoise.models import Model

class User(Model):
  user_id = fields.TextField(pk=True)
  name = fields.TextField()
  xp = fields.IntField()
  level = fields.IntField()


class Tag(Model):
  server = fields.TextField()
  creator = fields.ForeignKeyField("models.User", related_name="tags")
  name = fields.TextField()
  content = fields.TextField()
  time_created = fields.DatetimeField(auto_now_add=True)
  time_edited = fields.DatetimeField(auto_add=True)
