from abc import ABC, abstractmethod
from uuid import UUID


class PaymentGatewayInterface(ABC):
    @abstractmethod
    def get_checkout_link(self, sale_id: UUID) -> str:
        pass


class MockPaymentGateway(PaymentGatewayInterface):
    def get_checkout_link(self, sale_id):
        checkout_link = (
            f"https://mock-payment-gateway/get-checkout-link?sale-id={sale_id}"
        )
        return checkout_link


def provide_payment_gateway() -> PaymentGatewayInterface:
    return MockPaymentGateway()
