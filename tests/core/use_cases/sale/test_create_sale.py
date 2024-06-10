from datetime import datetime
from uuid import UUID, uuid4

from unittest.mock import MagicMock
import pytest
import pytz

from src.core.domain.aggregates.sale.value_objects.cpf import Cpf
from src.core.domain.aggregates.sale.value_objects.payment_status import PaymentStatus
from src.core.use_cases.sale.create import CreateSaleInteractor
from src.interface_adapters.dtos.sale.create import (
    CreateSaleInputDTO,
    CreateSaleOutputDTO,
)
from src.interface_adapters.gateways.payment_gateway import PaymentGatewayInterface
from src.interface_adapters.gateways.repositories.sale import SaleRepositoryInterface


@pytest.fixture
def mock_sale_repository():
    return MagicMock(spec=SaleRepositoryInterface)


@pytest.fixture
def mock_payment_gateway():
    return MagicMock(spec=PaymentGatewayInterface)


@pytest.fixture
def create_sale_interactor(mock_sale_repository, mock_payment_gateway):
    return CreateSaleInteractor(
        sale_repository=mock_sale_repository, payment_gateway=mock_payment_gateway
    )


@pytest.fixture
def example_create_sale_input_dto():
    return CreateSaleInputDTO(vehicle_id=uuid4(), buyer_cpf="45040360029")


@pytest.fixture
def example_create_sale_output_dto():
    return CreateSaleOutputDTO(
        id=uuid4(),
        vehicle_id=UUID("ad64017e-771e-4e83-9152-732b69719f06"),
        buyer_cpf=Cpf("45040360029").value,
        sale_datetime=datetime.now(pytz.UTC),
        payment_status=PaymentStatus.PENDING.value,
        checkout_link="https://example.com/checkout",
    )


@pytest.mark.asyncio
async def test_execute_creates_new_sale(
    create_sale_interactor,
    example_create_sale_input_dto,
    example_create_sale_output_dto,
    mock_sale_repository,
    mock_payment_gateway,
):
    mock_payment_gateway.get_checkout_link.return_value = (
        example_create_sale_output_dto.checkout_link
    )

    output_dto = await create_sale_interactor.execute(example_create_sale_input_dto)

    assert isinstance(output_dto, CreateSaleOutputDTO)
    assert output_dto.id is not None
    assert output_dto.vehicle_id == example_create_sale_input_dto.vehicle_id
    assert output_dto.buyer_cpf == Cpf(example_create_sale_input_dto.buyer_cpf).value
    assert output_dto.sale_datetime is not None
    assert output_dto.payment_status == PaymentStatus.PENDING.value
    assert output_dto.checkout_link == example_create_sale_output_dto.checkout_link

    mock_payment_gateway.get_checkout_link.assert_called_once_with(
        sale_id=output_dto.id
    )
    mock_sale_repository.create.assert_called_once_with(dto=output_dto)
