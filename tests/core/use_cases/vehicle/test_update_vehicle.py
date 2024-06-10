from uuid import uuid4

import pytest
from unittest.mock import MagicMock

from src.core.use_cases.vehicle.update import UpdateVehicleInteractor
from src.interface_adapters.dtos.vehicle.update import UpdateVehicleDTO
from src.interface_adapters.gateways.repositories.vehicle import (
    VehicleRepositoryInterface,
)


@pytest.fixture
def mock_vehicle_repository():
    return MagicMock(spec=VehicleRepositoryInterface)


@pytest.fixture
def update_vehicle_interactor(mock_vehicle_repository):
    return UpdateVehicleInteractor(vehicle_repository=mock_vehicle_repository)


@pytest.fixture
def example_update_vehicle_input_dto():
    return UpdateVehicleDTO(
        status="SOLD",
        make="Toyota",
        model="Camry",
        color="Red",
        year=2021,
        kilometerage=20000,
        price_cents=2500000,
    )


@pytest.mark.asyncio
async def test_execute_updates_existing_vehicle(
    update_vehicle_interactor, example_update_vehicle_input_dto, mock_vehicle_repository
):
    vehicle_id = uuid4()

    output_dto = await update_vehicle_interactor.execute(
        id=vehicle_id, input_dto=example_update_vehicle_input_dto
    )

    assert isinstance(output_dto, UpdateVehicleDTO)
    assert output_dto.status == example_update_vehicle_input_dto.status
    assert output_dto.make == example_update_vehicle_input_dto.make
    assert output_dto.model == example_update_vehicle_input_dto.model
    assert output_dto.color == example_update_vehicle_input_dto.color
    assert output_dto.year == example_update_vehicle_input_dto.year
    assert output_dto.kilometerage == example_update_vehicle_input_dto.kilometerage
    assert output_dto.price_cents == example_update_vehicle_input_dto.price_cents

    mock_vehicle_repository.update.assert_called_once_with(
        id=vehicle_id, dto=example_update_vehicle_input_dto
    )
