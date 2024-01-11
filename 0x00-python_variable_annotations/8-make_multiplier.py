#!/usr/bin/env python3
"""Complex types - functions module"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Function that takes a float multiplier as argument and returns a function
    that multiplies a float by multiplier.
    """
    def multiply_by_multiplier(num: float) -> float:
        """
        Function that multiplies a float n by multiplier.
        """
        return num * multiplier
    return multiply_by_multiplier
