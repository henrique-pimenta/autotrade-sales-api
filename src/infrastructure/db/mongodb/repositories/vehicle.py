from dataclasses import asdict

from src.infrastructure.db.mongodb.connection import get_collection
from src.interface_adapters.dtos.vehicle.read import ReadVehicleOutputDTO
from src.interface_adapters.gateways.repositories.vehicle import (
    VehicleRepositoryInterface,
)


class VehicleRepository(VehicleRepositoryInterface):
    def __init__(self, collection=None):
        self._collection = collection or get_collection("vehicles")

    async def create(self, dto):
        document = asdict(dto)
        document["id"] = str(document["id"])
        await self._collection.insert_one(document)

    async def list(self, filter_query):
        ascending = 1
        cursor = self._collection.find(filter_query).sort("price_cents", ascending)
        documents = await cursor.to_list(length=None)
        return [
            ReadVehicleOutputDTO(
                id=doc["id"],
                status=doc["status"],
                make=doc["make"],
                model=doc["model"],
                color=doc["color"],
                year=doc["year"],
                kilometerage=doc["kilometerage"],
                price_cents=doc["price_cents"],
            )
            for doc in documents
        ]

    async def update(self, id, dto):
        partial_document = asdict(
            dto, dict_factory=lambda x: {k: v for (k, v) in x if v is not None}
        )
        await self._collection.update_one({"id": str(id)}, {"$set": partial_document})


def provide_vehicle_repository() -> VehicleRepositoryInterface:
    return VehicleRepository()
