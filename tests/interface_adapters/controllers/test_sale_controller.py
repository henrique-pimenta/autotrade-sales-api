from datetime import datetime
from uuid import UUID

import pytest
from unittest.mock import AsyncMock, MagicMock

from src.interface_adapters.controllers.sale import SaleController
from src.interface_adapters.dtos.sale.create import CreateSaleOutputDTO
from src.interface_adapters.gateways.admin_service import AdminServiceGatewayInterface
from src.interface_adapters.gateways.payment_gateway import PaymentGatewayInterface
from src.interface_adapters.models.sale import SaleCreateInputModel
from src.interface_adapters.presenters.sale import SalePresenter


@pytest.fixture
def mock_sale_repository():
    return AsyncMock()


@pytest.fixture
def mock_payment_gateway():
    return MagicMock(spec=PaymentGatewayInterface)


@pytest.fixture
def mock_admin_service_gateway():
    return MagicMock(spec=AdminServiceGatewayInterface)


@pytest.fixture
def sale_controller(mock_sale_repository):
    return SaleController(sale_repository=mock_sale_repository)


@pytest.mark.asyncio
async def test_create_sale(sale_controller, mock_payment_gateway):
    input_data = SaleCreateInputModel(
        vehicle_id=UUID("123e4567-e89b-12d3-a456-426614174000"), buyer_cpf="45040360029"
    )
    output_dto = CreateSaleOutputDTO(
        id=UUID("123e4567-e89b-12d3-a456-426614174001"),
        vehicle_id=UUID("123e4567-e89b-12d3-a456-426614174000"),
        buyer_cpf="45040360029",
        sale_datetime=datetime.now(),
        payment_status="pending",
        checkout_link="https://example.com/checkout",
    )
    mock_payment_gateway.get_checkout_link.return_value = "https://example.com/checkout"

    result = await sale_controller.create(input_data, mock_payment_gateway)

    presenter_result = SalePresenter.format_create_response_for_pydantic(dto=output_dto)
    assert result.payment_status == presenter_result.payment_status
    assert result.checkout_link == presenter_result.checkout_link
