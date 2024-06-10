import pytest

from src.core.domain.aggregates.sale.interfaces.value_objects import CpfInterface
from src.core.domain.aggregates.sale.validators.cpf import CpfValidator
from src.core.domain.shared.exceptions.sale import InvalidCPFException


class MockCpf(CpfInterface):
    def __init__(self, value: str):
        self._value = value
        self._validator = CpfValidator(self)

    @property
    def value(self):
        return self._value

    @property
    def validator(self):
        return self._validator


@pytest.fixture
def valid_cpf():
    return MockCpf("45040360029")


@pytest.fixture
def invalid_cpf_format():
    return MockCpf("123.456.789-00")


@pytest.fixture
def invalid_cpf_digits():
    return MockCpf("000.000.000-00")


@pytest.fixture
def invalid_cpf_repeated_digits():
    return MockCpf("11111111111")


@pytest.fixture
def cpf_validator(valid_cpf):
    return CpfValidator(valid_cpf)


def test_valid_cpf_validation(cpf_validator):
    assert cpf_validator.validate() is None


def test_invalid_cpf_format_validation(invalid_cpf_format):
    cpf_validator = CpfValidator(invalid_cpf_format)
    with pytest.raises(InvalidCPFException):
        cpf_validator.validate()


def test_invalid_cpf_digits_validation(invalid_cpf_digits):
    cpf_validator = CpfValidator(invalid_cpf_digits)
    with pytest.raises(InvalidCPFException):
        cpf_validator.validate()


def test_invalid_cpf_repeated_digits_validation(invalid_cpf_repeated_digits):
    cpf_validator = CpfValidator(invalid_cpf_repeated_digits)
    with pytest.raises(InvalidCPFException):
        cpf_validator.validate()


def test_invalid_cpf_type_validation():
    with pytest.raises(TypeError):
        CpfValidator("invalid_cpf_instance")
