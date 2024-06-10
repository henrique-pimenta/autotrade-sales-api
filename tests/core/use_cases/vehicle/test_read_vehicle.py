from uuid import uuid4

import pytest
from unittest.mock import MagicMock

from src.core.use_cases.vehicle.read import ListVehicleInteractor
from src.interface_adapters.dtos.vehicle.read import ReadVehicleOutputDTO
from src.interface_adapters.gateways.repositories.vehicle import (
    VehicleRepositoryInterface,
)
from src.core.domain.aggregates.vehicle.value_objects.vehicle_status import (
    VehicleStatus,
)


@pytest.fixture
def mock_vehicle_repository():
    return MagicMock(spec=VehicleRepositoryInterface)


@pytest.fixture
def list_vehicle_interactor(mock_vehicle_repository):
    return ListVehicleInteractor(vehicle_repository=mock_vehicle_repository)


@pytest.mark.asyncio
async def test_execute_lists_vehicles(list_vehicle_interactor, mock_vehicle_repository):
    mock_vehicle_repository.list.return_value = [
        ReadVehicleOutputDTO(
            id=uuid4(),
            status=VehicleStatus.AVAILABLE.value,
            make="Toyota",
            model="Camry",
            color="Blue",
            year=2020,
            kilometerage=15000,
            price_cents=2000000,
        ),
        ReadVehicleOutputDTO(
            id=uuid4(),
            status=VehicleStatus.SOLD.value,
            make="Honda",
            model="Civic",
            color="Red",
            year=2018,
            kilometerage=18000,
            price_cents=1800000,
        ),
    ]

    output_dtos = await list_vehicle_interactor.execute(sold=True)

    assert isinstance(output_dtos, list)
    assert len(output_dtos) == 2

    for dto in output_dtos:
        assert isinstance(dto, ReadVehicleOutputDTO)

    mock_vehicle_repository.list.assert_called_once_with(
        filter_query={"status": VehicleStatus.SOLD.value}
    )


@pytest.mark.asyncio
async def test_execute_lists_all_vehicles(
    list_vehicle_interactor, mock_vehicle_repository
):
    mock_vehicle_repository.list.return_value = [
        ReadVehicleOutputDTO(
            id=uuid4(),
            status=VehicleStatus.AVAILABLE.value,
            make="Toyota",
            model="Camry",
            color="Blue",
            year=2020,
            kilometerage=15000,
            price_cents=2000000,
        ),
        ReadVehicleOutputDTO(
            id=uuid4(),
            status=VehicleStatus.SOLD.value,
            make="Honda",
            model="Civic",
            color="Red",
            year=2018,
            kilometerage=18000,
            price_cents=1800000,
        ),
    ]

    output_dtos = await list_vehicle_interactor.execute(sold=None)

    assert isinstance(output_dtos, list)
    assert len(output_dtos) == 2

    for dto in output_dtos:
        assert isinstance(dto, ReadVehicleOutputDTO)

    mock_vehicle_repository.list.assert_called_once_with(filter_query={})
