from functools import singledispatch

from .spec import Spec, AndSpec, OrSpec


__all__ = [
    'where_builder',
]


def where_builder():

    @singledispatch
    def build(spec: Spec, *args, **kwargs) -> dict:
        raise NotImplemented()

    @build.register
    def _(spec: AndSpec, *args, **kwargs) -> dict:
        return {
            '$and': [
                build(spec.spec1, *args, **kwargs),
                build(spec.spec2, *args, **kwargs)
            ]
        }

    @build.register
    def _(spec: OrSpec, *args, **kwargs) -> dict:
        return {
            '$or': [
                build(spec.spec1, *args, **kwargs),
                build(spec.spec2, *args, **kwargs)
            ]
        }

    return build
