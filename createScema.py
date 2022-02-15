from tortoise import Tortoise, run_async
from connectToDatabase import connectToDatabase

async def main():
  await connectToDatabase()
  await Tortoise.generate_schemas()
  print("database schemas generated")
  
if __name__ == '__main__':
  run_async(main())
