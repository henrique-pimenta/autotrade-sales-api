from src.core.domain.shared.exceptions.base import DomainException


class InvalidCPFException(DomainException):
    def __init__(self, message="Invalid CPF"):
        super().__init__(message)
