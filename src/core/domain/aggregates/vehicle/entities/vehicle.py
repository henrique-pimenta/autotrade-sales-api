from uuid import UUID

from src.core.domain.aggregates.vehicle.interfaces.vehicle import VehicleInterface
from src.core.domain.aggregates.vehicle.value_objects.vehicle_status import (
    VehicleStatus,
)


class Vehicle(VehicleInterface):
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
        self._id = id
        self._status = status
        self._make = make
        self._model = model
        self._color = color
        self._year = year
        self._kilometerage = kilometerage
        self._price_cents = price_cents

    @property
    def id(self):
        return self._id

    @property
    def status(self):
        return self._status.value

    @property
    def make(self):
        return self._make

    @property
    def model(self):
        return self._model

    @property
    def color(self):
        return self._color

    @property
    def year(self):
        return self._year

    @property
    def kilometerage(self):
        return self._kilometerage

    @property
    def price_cents(self):
        return self._price_cents
