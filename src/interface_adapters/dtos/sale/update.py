from dataclasses import dataclass
from typing import Optional


@dataclass
class UpdateSaleDTO:
    payment_status: Optional[str] = None
