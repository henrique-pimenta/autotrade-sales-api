from datetime import datetime
from uuid import UUID

import pytest
from unittest.mock import AsyncMock, MagicMock

from src.infrastructure.db.mongodb.repositories.vehicle import VehicleRepository
from src.interface_adapters.dtos.vehicle.read import ReadVehicleOutputDTO
from src.interface_adapters.dtos.vehicle.update import UpdateVehicleDTO


@pytest.fixture
def mock_mongo_collection():
    return AsyncMock()


@pytest.fixture
def vehicle_repository(mock_mongo_collection):
    repo = VehicleRepository()
    repo._collection = mock_mongo_collection
    return repo


@pytest.mark.asyncio
async def test_create_vehicle(mock_mongo_collection, vehicle_repository):
    dto = ReadVehicleOutputDTO(
        id=UUID("123e4567-e89b-12d3-a456-426614174001"),
        status="available",
        make="Fiat",
        model="Mobi",
        color="gray",
        year=2022,
        kilometerage=56781,
        price_cents=5289000,
    )

    await vehicle_repository.create(dto)

    mock_mongo_collection.insert_one.assert_called_once()
    inserted_document = mock_mongo_collection.insert_one.call_args[0][0]
    assert inserted_document["id"] == str(dto.id)
    assert inserted_document["status"] == dto.status
    assert inserted_document["make"] == dto.make
    assert inserted_document["model"] == dto.model
    assert inserted_document["color"] == dto.color
    assert inserted_document["year"] == dto.year
    assert inserted_document["kilometerage"] == dto.kilometerage
    assert inserted_document["price_cents"] == dto.price_cents


@pytest.mark.asyncio
async def test_list_vehicles(mock_mongo_collection, vehicle_repository):
    mock_documents = [
        {
            "id": "123e4567-e89b-12d3-a456-426614174001",
            "status": "available",
            "make": "Fiat",
            "model": "Mobi",
            "color": "gray",
            "year": 2022,
            "kilometerage": 56781,
            "price_cents": 5289000,
        }
    ]
    mock_mongo_collection.find = MagicMock
    mock_mongo_collection.find.sort = MagicMock
    mock_mongo_collection.find.sort.to_list = AsyncMock(return_value=mock_documents)

    result = await vehicle_repository.list(filter_query={})

    assert len(result) == 1
    assert result[0].id == mock_documents[0]["id"]
    assert result[0].status == mock_documents[0]["status"]
    assert result[0].make == mock_documents[0]["make"]
    assert result[0].model == mock_documents[0]["model"]
    assert result[0].color == mock_documents[0]["color"]
    assert result[0].year == mock_documents[0]["year"]
    assert result[0].kilometerage == mock_documents[0]["kilometerage"]
    assert result[0].price_cents == mock_documents[0]["price_cents"]


@pytest.mark.asyncio
async def test_update_vehicle(mock_mongo_collection, vehicle_repository):
    vehicle_id = "123e4567-e89b-12d3-a456-426614174001"
    dto = UpdateVehicleDTO(make="Ford", model="Mustang")

    await vehicle_repository.update(vehicle_id, dto)

    mock_mongo_collection.update_one.assert_called_once_with(
        {"id": vehicle_id},
        {"$set": {"make": dto.make, "model": dto.model}},
    )
