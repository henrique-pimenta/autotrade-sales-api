from dataclasses import asdict

from src.infrastructure.db.mongodb.connection import get_collection
from src.interface_adapters.dtos.sale.read import ReadSaleOutputDTO
from src.interface_adapters.gateways.repositories.sale import SaleRepositoryInterface


class SaleRepository(SaleRepositoryInterface):
    def __init__(self):
        self._collection = get_collection("sales")

    async def create(self, dto):
        document = asdict(dto)
        document["id"] = str(document["id"])
        document["vehicle_id"] = str(document["vehicle_id"])
        await self._collection.insert_one(document)

    async def list(self, filter_query):
        cursor = self._collection.find(filter_query)
        documents = await cursor.to_list(length=None)
        return [
            ReadSaleOutputDTO(
                id=doc["id"],
                vehicle_id=doc["vehicle_id"],
                buyer_cpf=doc["buyer_cpf"],
                sale_datetime=doc["sale_datetime"],
                payment_status=doc["payment_status"],
            )
            for doc in documents
        ]


def provide_sale_repository() -> SaleRepositoryInterface:
    return SaleRepository()
