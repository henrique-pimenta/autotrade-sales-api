from uuid import UUID

from src.interface_adapters.dtos.vehicle.update import UpdateVehicleDTO
from src.interface_adapters.gateways.repositories.vehicle import (
    VehicleRepositoryInterface,
)


class UpdateVehicleInteractor:
    def __init__(
        self,
        vehicle_repository: VehicleRepositoryInterface,
    ):
        self._vehicle_repository = vehicle_repository

    async def execute(self, id: UUID, input_dto: UpdateVehicleDTO) -> UpdateVehicleDTO:
        output_dto = input_dto

        await self._vehicle_repository.update(id=id, dto=output_dto)

        return output_dto
