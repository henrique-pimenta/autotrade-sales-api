from dataclasses import dataclass
from uuid import UUID


@dataclass
class CreateVehicleInputDTO:
    id: UUID
    make: str
    model: str
    color: str
    year: int
    kilometerage: int
    price_cents: int


@dataclass
class CreateVehicleOutputDTO:
    id: UUID
    status: str
    make: str
    model: str
    color: str
    year: int
    kilometerage: int
    price_cents: int
