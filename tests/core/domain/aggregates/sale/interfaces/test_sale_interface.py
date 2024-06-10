from datetime import datetime
from uuid import UUID, uuid4

import pytest

from src.core.domain.aggregates.sale.interfaces.sale import SaleInterface
from src.core.domain.aggregates.sale.interfaces.value_objects import CpfInterface
from src.core.domain.aggregates.sale.value_objects.cpf import Cpf
from src.core.domain.aggregates.sale.value_objects.payment_status import PaymentStatus
from src.core.domain.shared.exceptions.base import InvalidUUIDException
from src.core.domain.shared.exceptions.sale import InvalidCPFException


class ConcreteSale(SaleInterface):
    def __init__(
        self,
        id: UUID,
        vehicle_id: UUID,
        buyer_cpf: CpfInterface,
        sale_datetime: datetime,
        payment_status: PaymentStatus,
    ):
        if not isinstance(id, UUID):
            raise InvalidUUIDException
        if not isinstance(vehicle_id, UUID):
            raise InvalidUUIDException
        if not isinstance(buyer_cpf, CpfInterface):
            raise InvalidCPFException
        if not isinstance(payment_status, PaymentStatus):
            raise ValueError("Invalid status")
        self._id = id
        self._vehicle_id = vehicle_id
        self._buyer_cpf = buyer_cpf
        self._sale_datetime = sale_datetime
        self._payment_status = payment_status

    @property
    def id(self) -> UUID:
        return self._id

    @property
    def vehicle_id(self) -> UUID:
        return self._vehicle_id

    @property
    def buyer_cpf(self) -> str:
        return self._buyer_cpf.value

    @property
    def sale_datetime(self) -> datetime:
        return self._sale_datetime

    @property
    def payment_status(self) -> str:
        return self._payment_status.value


@pytest.fixture
def sale():
    return ConcreteSale(
        id=uuid4(),
        vehicle_id=uuid4(),
        buyer_cpf=Cpf("45040360029"),
        sale_datetime=datetime.now(),
        payment_status=PaymentStatus.PENDING,
    )


def test_sale_id(sale):
    assert isinstance(sale.id, UUID)


def test_sale_vehicle_id(sale):
    assert isinstance(sale.vehicle_id, UUID)


def test_sale_buyer_cpf(sale):
    assert isinstance(sale.buyer_cpf, str)
    assert sale.buyer_cpf == "45040360029"


def test_sale_sale_datetime(sale):
    assert isinstance(sale.sale_datetime, datetime)


def test_sale_payment_status(sale):
    assert isinstance(sale.payment_status, str)
    assert sale.payment_status == PaymentStatus.PENDING.value


def test_sale_datetime_immutable(sale):
    with pytest.raises(AttributeError):
        sale.sale_datetime = datetime.now()


def test_invalid_sale_id():
    with pytest.raises(InvalidUUIDException):
        ConcreteSale(
            id="invalid_id",
            vehicle_id=uuid4(),
            buyer_cpf=Cpf("45040360029"),
            sale_datetime=datetime.now(),
            payment_status=PaymentStatus.PENDING,
        )


def test_invalid_sale_vehicle_id():
    with pytest.raises(InvalidUUIDException):
        ConcreteSale(
            id=uuid4(),
            vehicle_id="invalid_vehicle_id",
            buyer_cpf=Cpf("45040360029"),
            sale_datetime=datetime.now(),
            payment_status=PaymentStatus.PENDING,
        )


def test_invalid_sale_buyer_cpf():
    with pytest.raises(InvalidCPFException):
        ConcreteSale(
            id=uuid4(),
            vehicle_id=uuid4(),
            buyer_cpf="450.403.600-29",
            sale_datetime=datetime.now(),
            payment_status=PaymentStatus.PENDING,
        )


# def test_sale_payment_status_enum():
#     valid_statuses = [status.value for status in PaymentStatus]
#     assert sale.payment_status in valid_statuses
