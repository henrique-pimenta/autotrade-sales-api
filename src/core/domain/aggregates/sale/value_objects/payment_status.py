from enum import Enum


class PaymentStatus(Enum):
    APPROVED = "approved"
    CANCELED = "canceled"
    PENDING = "pending"
