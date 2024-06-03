from src.core.domain.aggregates.sale.interfaces.value_objects import CpfInterface
from src.core.domain.aggregates.sale.validators.cpf import CpfValidator


class Cpf(CpfInterface):
    def __init__(self, value: str):
        self.value = value
        self._validator = CpfValidator(self)
        self.validator.validate()

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def validator(self):
        return self._validator
