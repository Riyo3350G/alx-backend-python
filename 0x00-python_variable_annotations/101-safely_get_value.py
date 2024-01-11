#!/usr/bin/env python3
"""Complex types - TypeVar & mapping module"""
from typing import Mapping, Any, TypeVar, Union


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None)\
        -> Union[Any, T]:
    """
    Function that takes a dict dct, a key and an optional argument default
    which is the type of the value to return.
    """
    if key in dct:
        return dct[key]
    else:
        return default
