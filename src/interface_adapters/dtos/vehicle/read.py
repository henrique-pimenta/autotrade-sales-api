from dataclasses import dataclass
from uuid import UUID


@dataclass
class ReadVehicleOutputDTO:
    id: UUID
    status: str
    make: str
    model: str
    color: str
    year: int
    kilometerage: int
    price_cents: int
