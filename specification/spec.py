from abc import ABC
from dataclasses import dataclass
from typing import TypeVar


__all__ = [
    'Spec',
]


T = TypeVar('T')


@dataclass
class Spec(ABC):

    def __or__(self, other):
        return OrSpec(self, other)

    def __and__(self, other):
        return AndSpec(self, other)

    def satisfy(self, model: T) -> bool:
        pass


class OrSpec(Spec):
    def __init__(self, spec1: Spec, spec2: Spec):
        self.spec1 = spec1
        self.spec2 = spec2

    def satisfy(self, model: T) -> bool:
        return self.spec1.satisfy(model) or self.spec2.satisfy(model)


class AndSpec(Spec):
    def __init__(self, spec1: Spec, spec2: Spec):
        self.spec1 = spec1
        self.spec2 = spec2

    def satisfy(self, model: T) -> bool:
        return self.spec1.satisfy(model) and self.spec2.satisfy(model)
