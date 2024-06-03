from abc import abstractmethod
from typing import List

from src.core.domain.shared.interfaces.repository import BaseRepositoryInterface
from src.interface_adapters.dtos.sale.create import CreateSaleOutputDTO
from src.interface_adapters.dtos.sale.read import ReadSaleOutputDTO


class SaleRepositoryInterface(
    BaseRepositoryInterface[CreateSaleOutputDTO, ReadSaleOutputDTO, None]
):
    @abstractmethod
    async def create(self, dto):
        pass

    @abstractmethod
    async def find_by_id(self, id):
        pass

    @abstractmethod
    async def list(self, filter_query) -> List[ReadSaleOutputDTO]:
        pass

    @abstractmethod
    async def update(self, id, dto):
        pass
