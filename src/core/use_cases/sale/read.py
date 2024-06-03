from typing import List

from src.interface_adapters.dtos.sale.read import ReadSaleOutputDTO
from src.interface_adapters.gateways.repositories.sale import SaleRepositoryInterface


class ListSaleInteractor:
    def __init__(
        self,
        sale_repository: SaleRepositoryInterface,
    ):
        self._sale_repository = sale_repository

    async def execute(self) -> List[ReadSaleOutputDTO]:
        output_dto = await self._sale_repository.list(filter_query={})
        return output_dto
