from uuid import UUID

import pytest
from unittest.mock import AsyncMock, MagicMock

from src.core.domain.aggregates.vehicle.value_objects.vehicle_status import (
    VehicleStatus,
)
from src.interface_adapters.controllers.vehicle import VehicleController
from src.interface_adapters.dtos.vehicle.read import ReadVehicleOutputDTO
from src.interface_adapters.gateways.repositories.vehicle import (
    VehicleRepositoryInterface,
)
from src.interface_adapters.models.vehicle import (
    VehicleFullModel,
    VehicleFullModelCollection,
)
from src.interface_adapters.presenters.vehicle import VehiclePresenter


@pytest.fixture
def mock_vehicle_repository():
    return AsyncMock(spec=VehicleRepositoryInterface)


@pytest.fixture
def vehicle_controller(mock_vehicle_repository):
    return VehicleController(vehicle_repository=mock_vehicle_repository)


@pytest.mark.asyncio
async def test_list_vehicles(vehicle_controller, mock_vehicle_repository):
    mock_output_dto = [
        ReadVehicleOutputDTO(
            id=UUID("123e4567-e89b-12d3-a456-426614174001"),
            status="sold",
            make="Fiat",
            model="Mobi",
            color="gray",
            year=2022,
            kilometerage=56781,
            price_cents=5289000,
        ),
        ReadVehicleOutputDTO(
            id=UUID("123e4567-e89b-12d3-a456-426614174002"),
            status="sold",
            make="Honda",
            model="Civic",
            color="red",
            year=2018,
            kilometerage=45000,
            price_cents=4000000,
        ),
    ]
    mock_vehicle_repository.list.return_value = mock_output_dto
    mock_formatted_result = VehicleFullModelCollection(
        vehicles=[
            VehicleFullModel(
                id=vehicle.id,
                status=vehicle.status,
                make=vehicle.make,
                model=vehicle.model,
                color=vehicle.color,
                year=vehicle.year,
                kilometerage=vehicle.kilometerage,
                price_cents=vehicle.price_cents,
            )
            for vehicle in mock_output_dto
        ]
    )
    VehiclePresenter.format_list_response_for_pydantic = MagicMock(
        return_value=mock_formatted_result
    )

    result = await vehicle_controller.list(sold=True)

    mock_vehicle_repository.list.assert_called_once_with(
        filter_query={"status": VehicleStatus.SOLD.value}
    )
    VehiclePresenter.format_list_response_for_pydantic.assert_called_once_with(
        dto=mock_output_dto
    )
    assert result == mock_formatted_result
