from uuid import UUID

from pydantic import BaseModel

from src.core.use_cases.vehicle.create import CreateVehicleInteractor
from src.core.use_cases.vehicle.read import ListVehicleInteractor
from src.core.use_cases.vehicle.update import UpdateVehicleInteractor
from src.interface_adapters.dtos.vehicle.create import CreateVehicleInputDTO
from src.interface_adapters.dtos.vehicle.update import UpdateVehicleDTO
from src.interface_adapters.gateways.repositories.vehicle import (
    VehicleRepositoryInterface,
)
from src.interface_adapters.models.shared import EmptyResponse
from src.interface_adapters.models.vehicle import (
    VehicleCreateInputModel,
    VehicleFullModelCollection,
    VehicleUpdateInputModel,
)
from src.interface_adapters.presenters.vehicle import VehiclePresenter


class VehicleController:
    def __init__(self, vehicle_repository: VehicleRepositoryInterface):
        self.vehicle_repository = vehicle_repository

    async def create(self, input_data: VehicleCreateInputModel) -> BaseModel:
        input_dto = CreateVehicleInputDTO(
            id=input_data.id,
            make=input_data.make,
            model=input_data.model,
            color=input_data.color,
            year=input_data.year,
            kilometerage=input_data.kilometerage,
            price_cents=input_data.price_cents,
        )
        await CreateVehicleInteractor(
            vehicle_repository=self.vehicle_repository
        ).execute(input_dto=input_dto)
        return EmptyResponse()

    async def list(self, sold: bool) -> VehicleFullModelCollection:
        output_dto = await ListVehicleInteractor(
            vehicle_repository=self.vehicle_repository
        ).execute(sold=sold)
        return VehiclePresenter.format_list_response_for_pydantic(dto=output_dto)

    async def update(self, id: UUID, input_data: VehicleUpdateInputModel) -> BaseModel:
        input_dto = UpdateVehicleDTO(**input_data.model_dump(exclude_unset=True))

        await UpdateVehicleInteractor(
            vehicle_repository=self.vehicle_repository
        ).execute(id=id, input_dto=input_dto)

        return EmptyResponse()
