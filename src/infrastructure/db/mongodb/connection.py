from decouple import config
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorCollection


def get_db_client():
    db_client = AsyncIOMotorClient(config("MONGODB_URL")).get_database("dev")
    return db_client


def get_collection(collection_name: str) -> AsyncIOMotorCollection:
    db_client = get_db_client()
    return db_client.get_collection(name=collection_name)
