from uuid import UUID

from src.core.domain.aggregates.sale.value_objects.payment_status import PaymentStatus
from src.core.domain.aggregates.vehicle.value_objects.vehicle_status import (
    VehicleStatus,
)
from src.core.domain.shared.exceptions.base import NotFoundException
from src.interface_adapters.dtos.sale.update import UpdateSaleDTO
from src.interface_adapters.gateways.admin_service import AdminServiceGatewayInterface
from src.interface_adapters.gateways.repositories.sale import (
    SaleRepositoryInterface,
)


class UpdateSaleInteractor:
    def __init__(
        self,
        sale_repository: SaleRepositoryInterface,
        admin_service_gateway: AdminServiceGatewayInterface,
    ):
        self._sale_repository = sale_repository
        self._admin_service_gateway = admin_service_gateway

    async def execute(self, id: UUID, input_dto: UpdateSaleDTO) -> UpdateSaleDTO:
        output_dto = input_dto

        read_sale_dto = await self._sale_repository.find_by_id(id=id)
        if not read_sale_dto:
            raise NotFoundException(message="Sale not found")

        await self._sale_repository.update(id=id, dto=output_dto)

        if PaymentStatus(output_dto.payment_status) == PaymentStatus.APPROVED:
            self._admin_service_gateway.update_vehicle_status(
                vehicle_id=read_sale_dto.vehicle_id, status=VehicleStatus.SOLD.value
            )

        return output_dto
