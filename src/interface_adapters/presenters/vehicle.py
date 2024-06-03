from typing import List

from src.interface_adapters.dtos.vehicle.read import ReadVehicleOutputDTO
from src.interface_adapters.models.vehicle import (
    VehicleFullModel,
    VehicleFullModelCollection,
)


class VehiclePresenter:
    @staticmethod
    def format_find_response_for_pydantic(
        dto: ReadVehicleOutputDTO,
    ) -> VehicleFullModel:
        return VehicleFullModel(
            id=dto.id,
            status=dto.status,
            make=dto.make,
            model=dto.model,
            color=dto.color,
            year=dto.year,
            kilometerage=dto.kilometerage,
            price_cents=dto.price_cents,
        )

    @staticmethod
    def format_list_response_for_pydantic(
        dto: List[ReadVehicleOutputDTO],
    ) -> VehicleFullModelCollection:
        return VehicleFullModelCollection(
            vehicles=[
                VehiclePresenter.format_find_response_for_pydantic(dto=vehicle_data)
                for vehicle_data in dto
            ]
        )
