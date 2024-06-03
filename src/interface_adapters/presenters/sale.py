from typing import List

from src.interface_adapters.dtos.sale.create import CreateSaleOutputDTO
from src.interface_adapters.dtos.sale.read import ReadSaleOutputDTO
from src.interface_adapters.models.sale import (
    SaleCreateOutputModel,
    SaleFullModel,
    SaleFullModelCollection,
)


class SalePresenter:
    @staticmethod
    def format_create_response_for_pydantic(
        dto: CreateSaleOutputDTO,
    ) -> SaleCreateOutputModel:
        return SaleCreateOutputModel(
            id=dto.id,
            sale_datetime=dto.sale_datetime,
            payment_status=dto.payment_status,
        )

    @staticmethod
    def format_find_response_for_pydantic(dto: ReadSaleOutputDTO) -> SaleFullModel:
        return SaleFullModel(
            id=dto.id,
            vehicle_id=dto.vehicle_id,
            buyer_cpf=dto.buyer_cpf,
            sale_datetime=dto.sale_datetime,
            payment_status=dto.payment_status,
        )

    @staticmethod
    def format_list_response_for_pydantic(
        dto: List[ReadSaleOutputDTO],
    ) -> SaleFullModelCollection:
        return SaleFullModelCollection(
            sales=[
                SalePresenter.format_find_response_for_pydantic(dto=vehicle_data)
                for vehicle_data in dto
            ]
        )
