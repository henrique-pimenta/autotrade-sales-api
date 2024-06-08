from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query, status
from pydantic import BaseModel

from src.infrastructure.db.mongodb.repositories.vehicle import (
    provide_vehicle_repository,
)
from src.interface_adapters.controllers.vehicle import VehicleController
from src.interface_adapters.fastapi.auth import provide_api_key_auth
from src.interface_adapters.gateways.repositories.vehicle import (
    VehicleRepositoryInterface,
)
from src.interface_adapters.models.vehicle import (
    VehicleCreateInputModel,
    VehicleFullModelCollection,
    VehicleUpdateInputModel,
)


router = APIRouter()


@router.post(
    "/",
    dependencies=[
        Depends(provide_api_key_auth("REQUESTS_FROM_ADMIN_TO_SALES_API_KEY"))
    ],
    response_description="Create vehicle",
    response_model=BaseModel,
    status_code=status.HTTP_200_OK,
)
async def create(
    input_data: VehicleCreateInputModel,
    vehicle_repository: VehicleRepositoryInterface = Depends(
        provide_vehicle_repository
    ),
):
    try:
        response = await VehicleController(
            vehicle_repository=vehicle_repository
        ).create(input_data=input_data)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error") from e


@router.get(
    "/",
    response_description="List vehicles",
    response_model=VehicleFullModelCollection,
    status_code=status.HTTP_200_OK,
)
async def list(
    sold: bool = Query(None, description="Filter by sold status"),
    vehicle_repository: VehicleRepositoryInterface = Depends(
        provide_vehicle_repository
    ),
):
    try:
        response = await VehicleController(vehicle_repository=vehicle_repository).list(
            sold=sold
        )
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error") from e


@router.patch(
    "/{id}",
    dependencies=[
        Depends(provide_api_key_auth("REQUESTS_FROM_ADMIN_TO_SALES_API_KEY"))
    ],
    response_description="Update vehicle",
    response_model=BaseModel,
    status_code=status.HTTP_200_OK,
)
async def update(
    id: UUID,
    input_data: VehicleUpdateInputModel,
    vehicle_repository: VehicleRepositoryInterface = Depends(
        provide_vehicle_repository
    ),
):
    try:
        response = await VehicleController(
            vehicle_repository=vehicle_repository
        ).update(id=id, input_data=input_data)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error") from e
