#!/usr/bin/env python3
"""Safe first element module"""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Function that takes a list lst of any type and returns the first element
    of the list.
    """
    if lst:
        return lst[0]
    else:
        return None
