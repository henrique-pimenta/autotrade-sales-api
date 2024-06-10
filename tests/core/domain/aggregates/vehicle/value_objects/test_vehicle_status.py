from src.core.domain.aggregates.vehicle.value_objects.vehicle_status import (
    VehicleStatus,
)


def test_vehicle_status_enum():
    assert VehicleStatus.AVAILABLE.value == "available"
    assert VehicleStatus.SOLD.value == "sold"

    assert VehicleStatus["AVAILABLE"] == VehicleStatus.AVAILABLE
    assert VehicleStatus["SOLD"] == VehicleStatus.SOLD

    assert VehicleStatus("available") == VehicleStatus.AVAILABLE
    assert VehicleStatus("sold") == VehicleStatus.SOLD


def test_vehicle_status_enum_members():
    assert len(VehicleStatus) == 2
    assert VehicleStatus.AVAILABLE in VehicleStatus
    assert VehicleStatus.SOLD in VehicleStatus


def test_vehicle_status_enum_strings():
    assert str(VehicleStatus.AVAILABLE) == "VehicleStatus.AVAILABLE"
    assert str(VehicleStatus.SOLD) == "VehicleStatus.SOLD"
