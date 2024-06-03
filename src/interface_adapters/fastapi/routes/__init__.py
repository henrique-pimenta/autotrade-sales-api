from fastapi import APIRouter

from .sales import router as sales_router
from .vehicles import router as vehicles_router


api_router = APIRouter(prefix="/api")


api_router.include_router(sales_router, prefix="/sales", tags=["Sales"])
api_router.include_router(vehicles_router, prefix="/vehicles", tags=["Vehicles"])
