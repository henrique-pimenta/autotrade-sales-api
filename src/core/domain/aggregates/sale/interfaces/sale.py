from abc import ABC, abstractmethod
from datetime import datetime
from uuid import UUID

from src.core.domain.aggregates.sale.interfaces.value_objects import CpfInterface
from src.core.domain.aggregates.sale.value_objects.payment_status import PaymentStatus


class SaleInterface(ABC):
    _id: UUID
    _vehicle_id: UUID
    _buyer_cpf: CpfInterface
    _sale_datetime: datetime
    _payment_status: PaymentStatus

    @property
    @abstractmethod
    def id(self) -> UUID:
        pass

    @property
    @abstractmethod
    def vehicle_id(self) -> UUID:
        pass

    @property
    @abstractmethod
    def buyer_cpf(self) -> str:
        pass

    @property
    def sale_datetime(self) -> datetime:
        return self.sale_datetime

    @property
    @abstractmethod
    def payment_status(self) -> str:
        pass
