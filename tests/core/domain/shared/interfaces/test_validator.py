import pytest
from abc import ABC

from src.core.domain.aggregates.sale.value_objects.cpf import Cpf
from src.core.domain.shared.interfaces.validator import ValidatorInterface


class ValidatorMock(ValidatorInterface):
    def __init__(self, domain_object: ABC):
        super().__init__(domain_object)

    def validate(self) -> None:
        pass


@pytest.fixture
def test_validator():
    obj = Cpf("45040360029")
    return ValidatorMock(obj)


def test_validator_init(test_validator):
    assert isinstance(test_validator, ValidatorInterface)


def test_validator_validate(test_validator):
    test_validator.validate()
