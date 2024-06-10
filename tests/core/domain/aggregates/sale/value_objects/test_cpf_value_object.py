import pytest

from src.core.domain.aggregates.sale.interfaces.value_objects import CpfInterface
from src.core.domain.aggregates.sale.validators.cpf import CpfValidator
from src.core.domain.aggregates.sale.value_objects.cpf import Cpf
from src.core.domain.shared.exceptions.sale import InvalidCPFException


@pytest.fixture
def valid_cpf():
    return Cpf("45040360029")


def test_valid_cpf_instance(valid_cpf):
    assert isinstance(valid_cpf, CpfInterface)


def test_valid_cpf_value(valid_cpf):
    assert valid_cpf.value == "45040360029"


def test_invalid_cpf_repeated_digits():
    with pytest.raises(InvalidCPFException):
        Cpf("11111111111")


def test_cpf_validator_instance():
    cpf = Cpf("45040360029")
    assert isinstance(cpf.validator, CpfValidator)


def test_cpf_validator_validation():
    cpf = Cpf("45040360029")
    assert cpf.validator.validate() is None


def test_cpf_invalid_initialization():
    with pytest.raises(InvalidCPFException):
        Cpf("invalid_cpf_format")
