from abc import abstractmethod
from typing import List

from src.core.domain.shared.interfaces.repository import BaseRepositoryInterface
from src.interface_adapters.dtos.vehicle.create import CreateVehicleOutputDTO
from src.interface_adapters.dtos.vehicle.read import ReadVehicleOutputDTO
from src.interface_adapters.dtos.vehicle.update import UpdateVehicleDTO


class VehicleRepositoryInterface(
    BaseRepositoryInterface[
        CreateVehicleOutputDTO, ReadVehicleOutputDTO, UpdateVehicleDTO
    ]
):
    @abstractmethod
    async def create(self, dto):
        pass

    @abstractmethod
    async def find_by_id(self, id):
        pass

    @abstractmethod
    async def list(self, filter_query) -> List[ReadVehicleOutputDTO]:
        pass

    @abstractmethod
    async def update(self, id, dto):
        pass
