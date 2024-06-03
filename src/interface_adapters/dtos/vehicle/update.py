from dataclasses import dataclass
from typing import Optional


@dataclass
class UpdateVehicleDTO:
    status: Optional[str] = None
    make: Optional[str] = None
    model: Optional[str] = None
    color: Optional[str] = None
    year: Optional[int] = None
    kilometerage: Optional[int] = None
    price_cents: Optional[int] = None
