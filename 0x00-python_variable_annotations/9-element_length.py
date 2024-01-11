#!/usr/bin/env python3
"""Element length module"""
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Function that takes a list lst of strings and returns a list of tuples
    containing the list and the length of the string at the index.
    """
    return [(i, len(i)) for i in lst]
