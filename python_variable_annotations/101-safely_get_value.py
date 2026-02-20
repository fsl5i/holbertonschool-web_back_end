#!/usr/bin/env python3
"""Add type annotations using TypeVar for safely_get_value."""

from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')  # generic type for default and return


def safely_get_value(
    dct: Mapping,
    key: Any,
    default: Union[T, None] = None
) -> Union[Any, T]:
    """Return the value for key if present, else return default."""
    if key in dct:
        return dct[key]
    return default
