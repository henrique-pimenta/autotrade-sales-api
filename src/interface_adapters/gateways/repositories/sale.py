from abc import abstractmethod
from typing import List

from src.core.domain.shared.interfaces.repository import BaseRepositoryInterface
from src.interface_adapters.dtos.sale.create import CreateSaleOutputDTO
from src.interface_adapters.dtos.sale.read import ReadSaleOutputDTO
from src.interface_adapters.dtos.sale.update import UpdateSaleDTO


class SaleRepositoryInterface(
    BaseRepositoryInterface[CreateSaleOutputDTO, ReadSaleOutputDTO, UpdateSaleDTO]
):
    @abstractmethod
    async def create(self, dto):
        pass

    @abstractmethod
    async def find_by_id(self, id) -> ReadSaleOutputDTO:
        pass

    @abstractmethod
    async def list(self, filter_query) -> List[ReadSaleOutputDTO]:
        pass

    @abstractmethod
    async def update(self, id, dto):
        pass
