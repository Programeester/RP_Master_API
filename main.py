from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from typing import Optional as opt
from connectToDatabase import connectToDatabase
from infoClasses import *
from models import *

app = FastAPI()

@app.on_event("startup")
async def start_app():
  await connectToDatabase()

@app.get("/")
async def home():
  return {"online" : True}

@app.post("/create_user")
async def create_user(user : UserInfo):
  try:
    created_user = User.create(**user)
    created_user.save()
    return {"created" : True}
  except Exception as e:
    return {"error" : e}

  
  @app.get("/all_users")
  async def all_users():
    users = [user for user in User.objects.get.all()]

register_tortoise(
  app,
  db_url="sqlite://db.sqlite3",
  modules={"models": ["models"]},
  generate_schemas=True,
  add_exception_handlers=True,
)
