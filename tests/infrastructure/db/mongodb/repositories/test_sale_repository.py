from datetime import datetime
from uuid import UUID

import pytest
from unittest.mock import AsyncMock, MagicMock

from src.infrastructure.db.mongodb.repositories.sale import SaleRepository
from src.interface_adapters.dtos.sale.read import ReadSaleOutputDTO
from src.interface_adapters.dtos.sale.update import UpdateSaleDTO


@pytest.fixture
def mock_mongo_collection():
    return AsyncMock()


@pytest.fixture
def sale_repository(mock_mongo_collection):
    repo = SaleRepository()
    repo._collection = mock_mongo_collection
    return repo


@pytest.mark.asyncio
async def test_create_sale(mock_mongo_collection, sale_repository):
    dto = ReadSaleOutputDTO(
        id=UUID("123e4567-e89b-12d3-a456-426614174001"),
        vehicle_id=UUID("123e4567-e89b-12d3-a456-426614174000"),
        buyer_cpf="45040360029",
        sale_datetime=datetime.now(),
        payment_status="pending",
    )

    await sale_repository.create(dto)

    mock_mongo_collection.insert_one.assert_called_once()
    inserted_document = mock_mongo_collection.insert_one.call_args[0][0]
    assert inserted_document["id"] == str(dto.id)
    assert inserted_document["vehicle_id"] == str(dto.vehicle_id)
    assert inserted_document["buyer_cpf"] == dto.buyer_cpf
    assert inserted_document["sale_datetime"] == dto.sale_datetime
    assert inserted_document["payment_status"] == dto.payment_status


@pytest.mark.asyncio
async def test_list_sales(mock_mongo_collection, sale_repository):
    mock_documents = [
        {
            "id": "123e4567-e89b-12d3-a456-426614174001",
            "vehicle_id": "123e4567-e89b-12d3-a456-426614174000",
            "buyer_cpf": "45040360029",
            "sale_datetime": datetime.now(),
            "payment_status": "pending",
        }
    ]
    mock_mongo_collection.find = MagicMock
    mock_mongo_collection.find.to_list = AsyncMock(return_value=mock_documents)

    result = await sale_repository.list(filter_query={})

    assert len(result) == 1
    assert result[0].id == mock_documents[0]["id"]
    assert result[0].vehicle_id == mock_documents[0]["vehicle_id"]
    assert result[0].buyer_cpf == mock_documents[0]["buyer_cpf"]
    assert result[0].sale_datetime == mock_documents[0]["sale_datetime"]
    assert result[0].payment_status == mock_documents[0]["payment_status"]


@pytest.mark.asyncio
async def test_update_sale(mock_mongo_collection, sale_repository):
    sale_id = "123e4567-e89b-12d3-a456-426614174001"
    dto = UpdateSaleDTO(payment_status="approved")

    await sale_repository.update(sale_id, dto)

    mock_mongo_collection.update_one.assert_called_once_with(
        {"id": sale_id}, {"$set": {"payment_status": dto.payment_status}}
    )
