from src.core.domain.aggregates.vehicle.entities.vehicle import Vehicle
from src.core.domain.aggregates.vehicle.value_objects.vehicle_status import (
    VehicleStatus,
)
from src.interface_adapters.dtos.vehicle.create import (
    CreateVehicleInputDTO,
    CreateVehicleOutputDTO,
)
from src.interface_adapters.gateways.repositories.vehicle import (
    VehicleRepositoryInterface,
)


class CreateVehicleInteractor:
    def __init__(
        self,
        vehicle_repository: VehicleRepositoryInterface,
    ):
        self._vehicle_repository = vehicle_repository

    async def execute(self, input_dto: CreateVehicleInputDTO) -> CreateVehicleOutputDTO:
        new_vehicle = Vehicle(
            id=input_dto.id,
            status=VehicleStatus.AVAILABLE,
            make=input_dto.make,
            model=input_dto.model,
            color=input_dto.color,
            year=input_dto.year,
            kilometerage=input_dto.kilometerage,
            price_cents=input_dto.price_cents,
        )

        output_dto = CreateVehicleOutputDTO(
            id=new_vehicle.id,
            status=new_vehicle.status,
            make=new_vehicle.make,
            model=new_vehicle.model,
            color=new_vehicle.color,
            year=new_vehicle.year,
            kilometerage=new_vehicle.kilometerage,
            price_cents=new_vehicle.price_cents,
        )

        await self._vehicle_repository.create(dto=output_dto)

        return output_dto
