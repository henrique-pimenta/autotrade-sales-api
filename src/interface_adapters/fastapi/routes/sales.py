from fastapi import APIRouter, Depends, HTTPException, status

from src.infrastructure.db.mongodb.repositories.sale import provide_sale_repository
from src.interface_adapters.gateways.repositories.sale import SaleRepositoryInterface
from src.interface_adapters.models.sale import (
    SaleCreateInputModel,
    SaleFullModel,
    SaleFullModelCollection,
)
from src.interface_adapters.controllers.sale import SaleController


router = APIRouter()


@router.post(
    "/",
    response_description="Create sale",
    response_model=SaleFullModel,
    status_code=status.HTTP_200_OK,
)
async def create(
    input_data: SaleCreateInputModel,
    sale_repository: SaleRepositoryInterface = Depends(provide_sale_repository),
):
    try:
        response = await SaleController(sale_repository=sale_repository).create(
            input_data=input_data
        )
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error") from e


@router.get(
    "/",
    response_description="List sales",
    response_model=SaleFullModelCollection,
    status_code=status.HTTP_200_OK,
)
async def list(
    sale_repository: SaleRepositoryInterface = Depends(provide_sale_repository),
):
    try:
        response = await SaleController(sale_repository=sale_repository).list()
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error") from e
