from datetime import datetime
from uuid import UUID

import pytest

from src.core.domain.aggregates.sale.entities.sale import Sale
from src.core.domain.aggregates.sale.value_objects.cpf import Cpf
from src.core.domain.aggregates.sale.value_objects.payment_status import PaymentStatus
from src.core.domain.shared.exceptions.base import InvalidUUIDException


@pytest.fixture
def valid_sale_id():
    return UUID("123e4567-e89b-12d3-a456-426614174000")


@pytest.fixture
def valid_vehicle_id():
    return UUID("223e4567-e89b-12d3-a456-426614174000")


@pytest.fixture
def valid_buyer_cpf():
    return Cpf("45040360029")


@pytest.fixture
def valid_sale_datetime():
    return datetime(2023, 6, 1, 10, 30)


@pytest.fixture
def valid_payment_status():
    return PaymentStatus.APPROVED


@pytest.fixture
def sale(
    valid_sale_id,
    valid_vehicle_id,
    valid_buyer_cpf,
    valid_sale_datetime,
    valid_payment_status,
):
    return Sale(
        id=valid_sale_id,
        vehicle_id=valid_vehicle_id,
        buyer_cpf=valid_buyer_cpf,
        sale_datetime=valid_sale_datetime,
        payment_status=valid_payment_status,
    )


def test_valid_sale_id(sale, valid_sale_id):
    assert sale.id == valid_sale_id


def test_valid_vehicle_id(sale, valid_vehicle_id):
    assert sale.vehicle_id == valid_vehicle_id


def test_valid_buyer_cpf(sale, valid_buyer_cpf):
    assert sale.buyer_cpf == valid_buyer_cpf.value


def test_valid_sale_datetime(sale, valid_sale_datetime):
    assert sale.sale_datetime == valid_sale_datetime


def test_valid_payment_status(sale, valid_payment_status):
    assert sale.payment_status == valid_payment_status.value


def test_invalid_sale_id_type(valid_vehicle_id, valid_buyer_cpf, valid_sale_datetime):
    with pytest.raises(InvalidUUIDException):
        Sale(
            id="invalid_id_type",
            vehicle_id=valid_vehicle_id,
            buyer_cpf=valid_buyer_cpf,
            sale_datetime=valid_sale_datetime,
            payment_status=PaymentStatus.APPROVED,
        )


def test_invalid_buyer_cpf_type(valid_sale_id, valid_vehicle_id, valid_sale_datetime):
    with pytest.raises(TypeError, match="Invalid cpf"):
        Sale(
            id=valid_sale_id,
            vehicle_id=valid_vehicle_id,
            buyer_cpf="invalid_cpf_type",
            sale_datetime=valid_sale_datetime,
            payment_status=PaymentStatus.PENDING,
        )


def test_invalid_payment_status(
    valid_sale_id, valid_vehicle_id, valid_buyer_cpf, valid_sale_datetime
):
    with pytest.raises(TypeError, match="Invalid payment status"):
        Sale(
            id=valid_sale_id,
            vehicle_id=valid_vehicle_id,
            buyer_cpf=valid_buyer_cpf,
            sale_datetime=valid_sale_datetime,
            payment_status="invalid_payment_status",
        )
