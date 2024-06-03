from abc import ABC, abstractmethod

from src.core.domain.shared.interfaces.validator import ValidatorInterface


class CpfInterface(ABC):
    _value: str

    @property
    @abstractmethod
    def value(self) -> str:
        pass

    @property
    @abstractmethod
    def validator(self) -> ValidatorInterface:
        pass
