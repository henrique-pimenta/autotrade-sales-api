from decouple import config
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorCollection


db = AsyncIOMotorClient(config("MONGODB_URL")).get_database("dev")


def get_collection(collection_name: str) -> AsyncIOMotorCollection:
    return db.get_collection(name=collection_name)
