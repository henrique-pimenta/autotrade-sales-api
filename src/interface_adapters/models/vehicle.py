from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class VehicleCreateInputModel(BaseModel):
    id: UUID = Field(...)
    make: str = Field(...)
    model: str = Field(...)
    color: str = Field(...)
    year: int = Field(...)
    kilometerage: int = Field(...)
    price_cents: int = Field(...)

    __config__ = ConfigDict(
        populate_by_name=True,
        json_schema_extra={
            "example": {
                "id": "62101eba-142e-43d0-9215-f5f4f0940358",
                "make": "Fiat",
                "model": "Mobi",
                "color": "gray",
                "year": 2022,
                "kilometerage": 56781,
                "price_cents": 5289000,
            },
        },
    )


class VehicleFullModel(BaseModel):
    id: UUID = Field(...)
    status: str = Field(...)
    make: str = Field(...)
    model: str = Field(...)
    color: str = Field(...)
    year: int = Field(...)
    kilometerage: int = Field(...)
    price_cents: int = Field(...)

    __config__ = ConfigDict(
        populate_by_name=True,
        json_schema_extra={
            "example": {
                "id": "62101eba-142e-43d0-9215-f5f4f0940358",
                "status": "available",
                "make": "Fiat",
                "model": "Mobi",
                "color": "gray",
                "year": 2022,
                "kilometerage": 56781,
                "price_cents": 5289000,
            },
        },
    )


class VehicleFullModelCollection(BaseModel):
    vehicles: List[VehicleFullModel]


class VehicleUpdateInputModel(BaseModel):
    make: Optional[str] = None
    model: Optional[str] = None
    color: Optional[str] = None
    year: Optional[int] = None
    kilometerage: Optional[int] = None
    price_cents: Optional[int] = None

    __config__ = ConfigDict(
        populate_by_name=True,
        json_schema_extra={
            "example": {
                "price_cents": 5089000,
            },
        },
    )
