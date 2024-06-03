from datetime import datetime
from uuid import UUID

from src.core.domain.aggregates.sale.value_objects.cpf import Cpf
from src.core.domain.aggregates.sale.value_objects.payment_status import PaymentStatus
from src.core.domain.aggregates.sale.interfaces.sale import SaleInterface


class Sale(SaleInterface):
    def __init__(
        self,
        id: UUID,
        vehicle_id: UUID,
        buyer_cpf: Cpf,
        sale_datetime: datetime,
        payment_status: PaymentStatus,
    ):
        self._id = id
        self._vehicle_id = vehicle_id
        self._buyer_cpf = buyer_cpf
        self._sale_datetime = sale_datetime
        self._payment_status = payment_status

    @property
    def id(self):
        return self._id

    @property
    def vehicle_id(self):
        return self._vehicle_id

    @property
    def buyer_cpf(self):
        return self._buyer_cpf.value

    @property
    def sale_datetime(self):
        return self._sale_datetime

    @property
    def payment_status(self):
        return self._payment_status.value
