from uuid import uuid4

import pytest
from unittest.mock import MagicMock

from src.core.domain.aggregates.vehicle.value_objects.vehicle_status import (
    VehicleStatus,
)
from src.core.use_cases.vehicle.create import CreateVehicleInteractor
from src.interface_adapters.dtos.vehicle.create import (
    CreateVehicleInputDTO,
    CreateVehicleOutputDTO,
)
from src.interface_adapters.gateways.repositories.vehicle import (
    VehicleRepositoryInterface,
)


@pytest.fixture
def mock_vehicle_repository():
    return MagicMock(spec=VehicleRepositoryInterface)


@pytest.fixture
def create_vehicle_interactor(mock_vehicle_repository):
    return CreateVehicleInteractor(vehicle_repository=mock_vehicle_repository)


@pytest.fixture
def example_create_vehicle_input_dto():
    return CreateVehicleInputDTO(
        id=uuid4(),
        make="Toyota",
        model="Camry",
        color="Blue",
        year=2020,
        kilometerage=15000,
        price_cents=2000000,
    )


@pytest.fixture
def example_create_vehicle_output_dto():
    return CreateVehicleOutputDTO(
        id=uuid4(),
        status=VehicleStatus.AVAILABLE.value,
        make="Toyota",
        model="Camry",
        color="Blue",
        year=2020,
        kilometerage=15000,
        price_cents=2000000,
    )


@pytest.mark.asyncio
async def test_execute_creates_new_vehicle(
    create_vehicle_interactor,
    example_create_vehicle_input_dto,
    example_create_vehicle_output_dto,
    mock_vehicle_repository,
):
    mock_vehicle_repository.create.return_value = None

    output_dto = await create_vehicle_interactor.execute(
        input_dto=example_create_vehicle_input_dto
    )

    assert isinstance(output_dto, CreateVehicleOutputDTO)
    assert output_dto.id == example_create_vehicle_input_dto.id
    assert output_dto.status == VehicleStatus.AVAILABLE.value
    assert output_dto.make == example_create_vehicle_input_dto.make
    assert output_dto.model == example_create_vehicle_input_dto.model
    assert output_dto.color == example_create_vehicle_input_dto.color
    assert output_dto.year == example_create_vehicle_input_dto.year
    assert output_dto.kilometerage == example_create_vehicle_input_dto.kilometerage
    assert output_dto.price_cents == example_create_vehicle_input_dto.price_cents

    mock_vehicle_repository.create.assert_called_once_with(dto=output_dto)
