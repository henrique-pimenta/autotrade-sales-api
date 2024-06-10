from uuid import UUID, uuid4

import pytest

from src.core.domain.aggregates.vehicle.value_objects.vehicle_status import (
    VehicleStatus,
)
from src.core.domain.aggregates.vehicle.interfaces.vehicle import VehicleInterface


class ConcreteVehicle(VehicleInterface):
    def __init__(
        self,
        id: UUID,
        status: VehicleStatus,
        make: str,
        model: str,
        color: str,
        year: int,
        kilometerage: int,
        price_cents: int,
    ):
        if not isinstance(id, UUID):
            raise ValueError("Invalid ID")
        if not isinstance(status, VehicleStatus):
            raise ValueError("Invalid status")
        self._id = id
        self._status = status
        self._make = make
        self._model = model
        self._color = color
        self._year = year
        self._kilometerage = kilometerage
        self._price_cents = price_cents

    @property
    def id(self) -> UUID:
        return self._id

    @property
    def status(self) -> VehicleStatus:
        return self._status

    @property
    def make(self) -> str:
        return self._make

    @property
    def model(self) -> str:
        return self._model

    @property
    def color(self) -> str:
        return self._color

    @property
    def year(self) -> int:
        return self._year

    @property
    def kilometerage(self) -> int:
        return self._kilometerage

    @property
    def price_cents(self) -> int:
        return self._price_cents

    def __eq__(self, other):
        if isinstance(other, ConcreteVehicle):
            return (
                self.id == other.id
                and self.status == other.status
                and self.make == other.make
                and self.model == other.model
                and self.color == other.color
                and self.year == other.year
                and self.kilometerage == other.kilometerage
                and self.price_cents == other.price_cents
            )
        return False

    def __ne__(self, other):
        return not self.__eq__(other)


@pytest.fixture
def vehicle():
    return ConcreteVehicle(
        id=uuid4(),
        status=VehicleStatus.AVAILABLE,
        make="Toyota",
        model="Corolla",
        color="Blue",
        year=2020,
        kilometerage=15000,
        price_cents=2000000,
    )


@pytest.fixture
def another_vehicle():
    return ConcreteVehicle(
        id=uuid4(),
        status=VehicleStatus.SOLD,
        make="Honda",
        model="Civic",
        color="Red",
        year=2021,
        kilometerage=5000,
        price_cents=2500000,
    )


def test_vehicle_id(vehicle):
    assert isinstance(vehicle.id, UUID)


def test_vehicle_status(vehicle):
    assert isinstance(vehicle.status, VehicleStatus)
    assert vehicle.status == VehicleStatus.AVAILABLE


def test_vehicle_make(vehicle):
    assert isinstance(vehicle.make, str)
    assert vehicle.make == "Toyota"


def test_vehicle_model(vehicle):
    assert isinstance(vehicle.model, str)
    assert vehicle.model == "Corolla"


def test_vehicle_color(vehicle):
    assert isinstance(vehicle.color, str)
    assert vehicle.color == "Blue"


def test_vehicle_year(vehicle):
    assert isinstance(vehicle.year, int)
    assert vehicle.year == 2020


def test_vehicle_kilometerage(vehicle):
    assert isinstance(vehicle.kilometerage, int)
    assert vehicle.kilometerage == 15000


def test_vehicle_price_cents(vehicle):
    assert isinstance(vehicle.price_cents, int)
    assert vehicle.price_cents == 2000000


def test_vehicle_equality(vehicle, another_vehicle):
    vehicle_copy = ConcreteVehicle(
        id=vehicle.id,
        status=vehicle.status,
        make=vehicle.make,
        model=vehicle.model,
        color=vehicle.color,
        year=vehicle.year,
        kilometerage=vehicle.kilometerage,
        price_cents=vehicle.price_cents,
    )
    assert vehicle == vehicle_copy
    assert vehicle != another_vehicle


def test_invalid_vehicle_id():
    with pytest.raises(ValueError):
        ConcreteVehicle(
            id="invalid_id",
            status=VehicleStatus.AVAILABLE,
            make="Toyota",
            model="Corolla",
            color="Blue",
            year=2020,
            kilometerage=15000,
            price_cents=2000000,
        )


def test_invalid_vehicle_status():
    with pytest.raises(ValueError):
        ConcreteVehicle(
            id=uuid4(),
            status="invalid_status",
            make="Toyota",
            model="Corolla",
            color="Blue",
            year=2020,
            kilometerage=15000,
            price_cents=2000000,
        )


def test_different_vehicle_statuses():
    vehicle = ConcreteVehicle(
        id=uuid4(),
        status=VehicleStatus.SOLD,
        make="Toyota",
        model="Corolla",
        color="Blue",
        year=2020,
        kilometerage=15000,
        price_cents=2000000,
    )
    assert vehicle.status == VehicleStatus.SOLD


def test_vehicle_edge_year():
    vehicle = ConcreteVehicle(
        id=uuid4(),
        status=VehicleStatus.AVAILABLE,
        make="Toyota",
        model="Corolla",
        color="Blue",
        year=0,
        kilometerage=15000,
        price_cents=2000000,
    )
    assert vehicle.year == 0


def test_vehicle_edge_kilometerage():
    vehicle = ConcreteVehicle(
        id=uuid4(),
        status=VehicleStatus.AVAILABLE,
        make="Toyota",
        model="Corolla",
        color="Blue",
        year=2020,
        kilometerage=0,
        price_cents=2000000,
    )
    assert vehicle.kilometerage == 0


def test_vehicle_edge_price_cents():
    vehicle = ConcreteVehicle(
        id=uuid4(),
        status=VehicleStatus.AVAILABLE,
        make="Toyota",
        model="Corolla",
        color="Blue",
        year=2020,
        kilometerage=15000,
        price_cents=0,
    )
    assert vehicle.price_cents == 0
