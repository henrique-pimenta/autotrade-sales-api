from typing import List

from src.core.domain.aggregates.vehicle.value_objects.vehicle_status import (
    VehicleStatus,
)
from src.interface_adapters.dtos.vehicle.read import ReadVehicleOutputDTO
from src.interface_adapters.gateways.repositories.vehicle import (
    VehicleRepositoryInterface,
)


class ListVehicleInteractor:
    def __init__(
        self,
        vehicle_repository: VehicleRepositoryInterface,
    ):
        self._vehicle_repository = vehicle_repository

    async def execute(self, sold: bool) -> List[ReadVehicleOutputDTO]:
        filter_query = {}
        if sold is not None:
            vehicle_status = VehicleStatus.SOLD if sold else VehicleStatus.AVAILABLE
            filter_query["status"] = vehicle_status.value

        output_dto = await self._vehicle_repository.list(filter_query=filter_query)

        return output_dto
