from abc import ABC, abstractmethod
from uuid import UUID

import requests
from decouple import config


class AdminServiceGatewayInterface(ABC):
    @abstractmethod
    def update_vehicle_status(self, vehicle_id: UUID, status: str) -> None:
        pass


class AdminServiceGateway(AdminServiceGatewayInterface):
    def __init__(
        self,
        base_url=config("ADMIN_SERVICE_BASE_URL"),
        headers={"Authorization": config("REQUESTS_FROM_SALES_TO_ADMIN_API_KEY")},
    ):
        self._base_url = base_url
        self._headers = headers

    def update_vehicle_status(self, vehicle_id, status):
        response = requests.patch(
            f"{self._base_url}/vehicles/{vehicle_id}/",
            json={"status": status},
            headers=self._headers,
        )
        response.raise_for_status()


def provide_admin_service_gateway() -> AdminServiceGatewayInterface:
    return AdminServiceGateway()
