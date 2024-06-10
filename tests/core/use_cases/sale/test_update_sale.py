from uuid import uuid4

import pytest
from unittest.mock import MagicMock

from src.core.domain.aggregates.sale.value_objects.payment_status import PaymentStatus
from src.core.domain.aggregates.vehicle.value_objects.vehicle_status import (
    VehicleStatus,
)
from src.core.domain.shared.exceptions.base import NotFoundException
from src.core.use_cases.sale.update import UpdateSaleInteractor
from src.interface_adapters.dtos.sale.update import UpdateSaleDTO
from src.interface_adapters.gateways.admin_service import AdminServiceGatewayInterface
from src.interface_adapters.gateways.repositories.sale import SaleRepositoryInterface


@pytest.fixture
def mock_sale_repository():
    return MagicMock(spec=SaleRepositoryInterface)


@pytest.fixture
def mock_admin_service_gateway():
    return MagicMock(spec=AdminServiceGatewayInterface)


@pytest.fixture
def update_sale_interactor(mock_sale_repository, mock_admin_service_gateway):
    return UpdateSaleInteractor(
        sale_repository=mock_sale_repository,
        admin_service_gateway=mock_admin_service_gateway,
    )


@pytest.fixture
def example_update_sale_input_dto():
    return UpdateSaleDTO(payment_status=PaymentStatus.PENDING.value)


@pytest.fixture
def example_read_sale_dto():
    return UpdateSaleDTO(payment_status=PaymentStatus.PENDING.value)


@pytest.mark.asyncio
async def test_execute_updates_existing_sale(
    update_sale_interactor,
    example_update_sale_input_dto,
    example_read_sale_dto,
    mock_sale_repository,
    mock_admin_service_gateway,
):
    sale_id = uuid4()
    example_read_sale_dto.payment_status = PaymentStatus.PENDING.value
    mock_sale_repository.find_by_id.return_value = example_read_sale_dto

    output_dto = await update_sale_interactor.execute(
        id=sale_id, input_dto=example_update_sale_input_dto
    )

    assert isinstance(output_dto, UpdateSaleDTO)
    assert output_dto.payment_status == example_update_sale_input_dto.payment_status

    mock_sale_repository.find_by_id.assert_called_once_with(id=sale_id)
    mock_sale_repository.update.assert_called_once_with(
        id=sale_id, dto=example_update_sale_input_dto
    )

    if example_update_sale_input_dto.payment_status == PaymentStatus.APPROVED.value:
        mock_admin_service_gateway.update_vehicle_status.assert_called_once_with(
            vehicle_id=example_read_sale_dto.id, status=VehicleStatus.SOLD.value
        )
    else:
        mock_admin_service_gateway.update_vehicle_status.assert_not_called()


@pytest.mark.asyncio
async def test_execute_raises_not_found_exception(
    update_sale_interactor,
    example_update_sale_input_dto,
    mock_sale_repository,
    mock_admin_service_gateway,
):
    sale_id = uuid4()
    mock_sale_repository.find_by_id.return_value = None

    with pytest.raises(NotFoundException):
        await update_sale_interactor.execute(
            id=sale_id, input_dto=example_update_sale_input_dto
        )

    mock_sale_repository.find_by_id.assert_called_once_with(id=sale_id)
    mock_sale_repository.update.assert_not_called()
    mock_admin_service_gateway.update_vehicle_status.assert_not_called()
