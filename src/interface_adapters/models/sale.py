from datetime import datetime
from typing import List
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class SaleCreateInputModel(BaseModel):
    vehicle_id: UUID = Field(...)
    buyer_cpf: str = Field(...)

    class ConfigDict:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "vehicle_id": "62101eba-142e-43d0-9215-f5f4f0940358",
                "buyer_cpf": "45040360029",
            },
        }


class SaleCreateOutputModel(BaseModel):
    id: UUID = Field(...)
    sale_datetime: datetime
    payment_status: str
    checkout_link: str


class SaleFullModel(BaseModel):
    id: UUID = Field(...)
    vehicle_id: UUID = Field(...)
    buyer_cpf: str = Field(...)
    sale_datetime: datetime
    payment_status: str

    __config__ = ConfigDict(
        populate_by_name=True,
        json_schema_extra={
            "example": {
                "id": "4f4e62a0-22f6-4960-9b7a-b7be327c2809",
                "vehicle_id": "62101eba-142e-43d0-9215-f5f4f0940358",
                "buyer_cpf": "45040360029",
                "sale_datetime": "2024-05-30T16:05:51.380984Z",
                "payment_status": "pending",
            },
        },
    )


class SaleFullModelCollection(BaseModel):
    sales: List[SaleFullModel]


class SaleUpdateInputModel(BaseModel):
    payment_status: str = Field(...)

    __config__ = ConfigDict(
        populate_by_name=True,
        json_schema_extra={
            "example": {
                "payment_status": "approved",
            },
        },
    )
