from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel

from src.infrastructure.db.mongodb.repositories.sale import provide_sale_repository
from src.interface_adapters.fastapi.auth import provide_api_key_auth
from src.interface_adapters.gateways.admin_service import (
    AdminServiceGatewayInterface,
    provide_admin_service_gateway,
)
from src.interface_adapters.gateways.payment_gateway import (
    PaymentGatewayInterface,
    provide_payment_gateway,
)
from src.interface_adapters.gateways.repositories.sale import SaleRepositoryInterface
from src.interface_adapters.models.sale import (
    SaleCreateInputModel,
    SaleCreateOutputModel,
    SaleUpdateInputModel,
)
from src.interface_adapters.controllers.sale import (
    SaleController,
    provide_sale_controller,
)


router = APIRouter()


@router.post(
    "/",
    response_description="Create sale",
    response_model=SaleCreateOutputModel,
    status_code=status.HTTP_200_OK,
)
async def create(
    input_data: SaleCreateInputModel,
    sale_controller: SaleController = Depends(provide_sale_controller),
    payment_gateway: PaymentGatewayInterface = Depends(provide_payment_gateway),
):
    try:
        response = await sale_controller.create(
            input_data=input_data,
            payment_gateway=payment_gateway,
        )
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error") from e


@router.patch(
    "/{id}",
    dependencies=[
        Depends(provide_api_key_auth("REQUESTS_FROM_PAYMENT_GATEWAY_TO_SALES_API_KEY"))
    ],
    response_description="Update sale",
    response_model=BaseModel,
    status_code=status.HTTP_200_OK,
)
async def update(
    id: UUID,
    input_data: SaleUpdateInputModel,
    sale_repository: SaleRepositoryInterface = Depends(provide_sale_repository),
    admin_service_gateway: AdminServiceGatewayInterface = Depends(
        provide_admin_service_gateway
    ),
):
    try:
        response = await SaleController(sale_repository=sale_repository).update(
            id=id,
            input_data=input_data,
            admin_service_gateway=admin_service_gateway,
        )
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error") from e
