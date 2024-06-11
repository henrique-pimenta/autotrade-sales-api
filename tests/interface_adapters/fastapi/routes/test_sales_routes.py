from datetime import datetime
from unittest.mock import AsyncMock, MagicMock
from uuid import uuid4

import pytest
import pytz
from fastapi import status
from fastapi.testclient import TestClient

from src.interface_adapters.fastapi.main import app
from src.interface_adapters.controllers.sale import (
    SaleController,
    provide_sale_controller,
)
from src.interface_adapters.gateways.payment_gateway import (
    PaymentGatewayInterface,
    provide_payment_gateway,
)
from src.interface_adapters.gateways.repositories.sale import SaleRepositoryInterface
from src.interface_adapters.models.sale import (
    SaleCreateInputModel,
    SaleCreateOutputModel,
)


@pytest.fixture
def mock_sale_repository():
    return MagicMock(spec=SaleRepositoryInterface)


@pytest.fixture
def mock_payment_gateway():
    return MagicMock(spec=PaymentGatewayInterface)


def test_create_route_success(mock_sale_repository, mock_payment_gateway):
    vehicle_id = uuid4()
    buyer_cpf = "45040360029"
    input_data = SaleCreateInputModel(vehicle_id=vehicle_id, buyer_cpf=buyer_cpf)

    sale_id = uuid4()
    sale_datetime = datetime.now(pytz.UTC)
    payment_status = "pending"
    checkout_link = f"https://example.com/get-checkout-link?sale-id={sale_id}"
    output_data = SaleCreateOutputModel(
        id=sale_id,
        sale_datetime=sale_datetime,
        payment_status=payment_status,
        checkout_link=checkout_link,
    )

    mock_controller = SaleController(sale_repository=mock_sale_repository)
    mock_controller.create = AsyncMock(return_value=output_data)

    app.dependency_overrides[provide_sale_controller] = lambda: mock_controller
    app.dependency_overrides[provide_payment_gateway] = lambda: mock_payment_gateway

    test_client = TestClient(app=app)
    input_data_dict = input_data.model_dump()
    input_data_dict["vehicle_id"] = str(input_data_dict["vehicle_id"])
    response = test_client.post("/api/sales/", json=input_data_dict)

    assert response.status_code == status.HTTP_200_OK
    output_data = output_data.model_dump()
    output_data["id"] = str(output_data["id"])
    output_data["sale_datetime"] = (
        output_data["sale_datetime"].strftime("%Y-%m-%dT%H:%M:%S.%f") + "Z"
    )
    assert response.json() == output_data
    mock_controller.create.assert_called_once_with(
        input_data=input_data, payment_gateway=mock_payment_gateway
    )


def test_create_route_exception(mock_sale_repository, mock_payment_gateway):
    vehicle_id = uuid4()
    buyer_cpf = "45040360029"
    input_data = SaleCreateInputModel(vehicle_id=vehicle_id, buyer_cpf=buyer_cpf)

    mock_controller = SaleController(sale_repository=mock_sale_repository)
    mock_controller.create = AsyncMock(side_effect=Exception("Mocked error"))

    app.dependency_overrides[provide_sale_controller] = lambda: mock_controller
    app.dependency_overrides[provide_payment_gateway] = lambda: mock_payment_gateway

    test_client = TestClient(app=app)
    input_data_dict = input_data.model_dump()
    input_data_dict["vehicle_id"] = str(input_data_dict["vehicle_id"])
    response = test_client.post("/api/sales/", json=input_data_dict)

    assert response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR
