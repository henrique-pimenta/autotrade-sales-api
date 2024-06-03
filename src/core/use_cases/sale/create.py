from datetime import datetime
from uuid import uuid4

import pytz

from src.core.domain.aggregates.sale.entities.sale import Sale
from src.core.domain.aggregates.sale.value_objects.cpf import Cpf
from src.core.domain.aggregates.sale.value_objects.payment_status import PaymentStatus
from src.interface_adapters.dtos.sale.create import (
    CreateSaleInputDTO,
    CreateSaleOutputDTO,
)
from src.interface_adapters.gateways.repositories.sale import SaleRepositoryInterface


class CreateSaleInteractor:
    def __init__(
        self,
        sale_repository: SaleRepositoryInterface,
    ):
        self._sale_repository = sale_repository

    async def execute(self, input_dto: CreateSaleInputDTO) -> CreateSaleOutputDTO:
        new_sale = Sale(
            id=uuid4(),
            vehicle_id=input_dto.vehicle_id,
            buyer_cpf=Cpf(input_dto.buyer_cpf),
            sale_datetime=datetime.now(pytz.UTC),
            payment_status=PaymentStatus.PENDING,
        )

        output_dto = CreateSaleOutputDTO(
            id=new_sale.id,
            sale_datetime=new_sale.sale_datetime,
            payment_status=new_sale.payment_status,
        )

        await self._sale_repository.create(dto=output_dto)

        return output_dto
