from abc import ABC, abstractmethod
from uuid import UUID

from src.core.domain.aggregates.vehicle.value_objects.vehicle_status import (
    VehicleStatus,
)


class VehicleInterface(ABC):
    _id: UUID
    _status: VehicleStatus
    _make: str
    _model: str
    _color: str
    _year: int
    _kilometerage: int
    _price_cents: int

    @property
    @abstractmethod
    def id(self) -> UUID:
        pass

    @property
    @abstractmethod
    def status(self) -> str:
        pass

    @property
    @abstractmethod
    def make(self) -> str:
        pass

    @property
    @abstractmethod
    def model(self) -> str:
        pass

    @property
    @abstractmethod
    def color(self) -> str:
        pass

    @property
    @abstractmethod
    def year(self) -> int:
        pass

    @property
    @abstractmethod
    def kilometerage(self) -> int:
        pass

    @property
    @abstractmethod
    def price_cents(self) -> int:
        pass
