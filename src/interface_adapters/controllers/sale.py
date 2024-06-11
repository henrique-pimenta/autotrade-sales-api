from uuid import UUID

from fastapi import Depends
from pydantic import BaseModel

from src.core.use_cases.sale.create import CreateSaleInteractor
from src.core.use_cases.sale.update import UpdateSaleInteractor
from src.infrastructure.db.mongodb.repositories.sale import provide_sale_repository
from src.interface_adapters.dtos.sale.create import CreateSaleInputDTO
from src.interface_adapters.dtos.sale.update import UpdateSaleDTO
from src.interface_adapters.gateways.admin_service import AdminServiceGatewayInterface
from src.interface_adapters.gateways.payment_gateway import PaymentGatewayInterface
from src.interface_adapters.gateways.repositories.sale import SaleRepositoryInterface
from src.interface_adapters.models.sale import (
    SaleCreateInputModel,
    SaleCreateOutputModel,
    SaleUpdateInputModel,
)
from src.interface_adapters.models.shared import EmptyResponse
from src.interface_adapters.presenters.sale import SalePresenter


class SaleController:
    def __init__(self, sale_repository: SaleRepositoryInterface):
        self.sale_repository = sale_repository

    async def create(
        self, input_data: SaleCreateInputModel, payment_gateway: PaymentGatewayInterface
    ) -> SaleCreateOutputModel:
        input_dto = CreateSaleInputDTO(
            vehicle_id=input_data.vehicle_id, buyer_cpf=input_data.buyer_cpf
        )
        output_dto = await CreateSaleInteractor(
            sale_repository=self.sale_repository,
            payment_gateway=payment_gateway,
        ).execute(input_dto=input_dto)
        return SalePresenter.format_create_response_for_pydantic(dto=output_dto)

    async def update(
        self,
        id: UUID,
        input_data: SaleUpdateInputModel,
        admin_service_gateway: AdminServiceGatewayInterface,
    ) -> BaseModel:
        input_dto = UpdateSaleDTO(**input_data.model_dump(exclude_unset=True))
        await UpdateSaleInteractor(
            sale_repository=self.sale_repository,
            admin_service_gateway=admin_service_gateway,
        ).execute(id=id, input_dto=input_dto)
        return EmptyResponse()


def provide_sale_controller(
    sale_repository: SaleRepositoryInterface = Depends(provide_sale_repository),
) -> SaleController:
    return SaleController(sale_repository=sale_repository)
