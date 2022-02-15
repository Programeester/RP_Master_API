from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from typing import Optional as opt
from connectToDatabase import connectToDatabase
from models import *

app = FastAPI()

@app.on_event("startup")
async def start_app():
  await connectToDatabase()

@app.get("/")
async def home():
  return {"online" : True}

register_tortoise(
  app,
  db_url="sqlite://db.sqlite3",
  modules={"models": ["models"]},
  generate_schemas=True,
  add_exception_handlers=True,
)
