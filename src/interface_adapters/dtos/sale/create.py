from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass
class CreateSaleInputDTO:
    vehicle_id: UUID
    buyer_cpf: str


@dataclass
class CreateSaleOutputDTO:
    id: UUID
    vehicle_id: UUID
    buyer_cpf: str
    sale_datetime: datetime
    payment_status: str
    checkout_link: str
