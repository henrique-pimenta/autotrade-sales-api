from src.core.use_cases.sale.create import CreateSaleInteractor
from src.core.use_cases.sale.read import ListSaleInteractor
from src.interface_adapters.dtos.sale.create import CreateSaleInputDTO
from src.interface_adapters.gateways.repositories.sale import SaleRepositoryInterface
from src.interface_adapters.models.sale import (
    SaleCreateInputModel,
    SaleCreateOutputModel,
    SaleFullModelCollection,
)
from src.interface_adapters.presenters.sale import SalePresenter


class SaleController:
    def __init__(self, sale_repository: SaleRepositoryInterface):
        self.sale_repository = sale_repository

    async def create(self, input_data: SaleCreateInputModel) -> SaleCreateOutputModel:
        input_dto = CreateSaleInputDTO(
            vehicle_id=input_data.vehicle_id, buyer_cpf=input_data.buyer_cpf
        )
        output_dto = await CreateSaleInteractor(
            sale_repository=self.sale_repository
        ).execute(input_dto=input_dto)
        return SalePresenter.format_create_response_for_pydantic(dto=output_dto)

    async def list(self) -> SaleFullModelCollection:
        output_dto = await ListSaleInteractor(
            sale_repository=self.sale_repository
        ).execute()
        return SalePresenter.format_list_response_for_pydantic(dto=output_dto)
