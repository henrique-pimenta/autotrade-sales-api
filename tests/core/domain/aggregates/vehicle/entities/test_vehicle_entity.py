from uuid import UUID, uuid4

import pytest

from src.core.domain.aggregates.vehicle.entities.vehicle import Vehicle
from src.core.domain.aggregates.vehicle.value_objects.vehicle_status import (
    VehicleStatus,
)


@pytest.fixture
def vehicle():
    return Vehicle(
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
    return Vehicle(
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
    assert isinstance(vehicle.status, str)
    assert vehicle.status == VehicleStatus.AVAILABLE.value


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


def test_invalid_vehicle_status():
    with pytest.raises(ValueError):
        Vehicle(
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
    vehicle = Vehicle(
        id=uuid4(),
        status=VehicleStatus.SOLD,
        make="Toyota",
        model="Corolla",
        color="Blue",
        year=2020,
        kilometerage=15000,
        price_cents=2000000,
    )
    assert vehicle.status == VehicleStatus.SOLD.value


def test_vehicle_edge_year():
    vehicle = Vehicle(
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
    vehicle = Vehicle(
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
    vehicle = Vehicle(
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
