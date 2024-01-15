#!/usr/bin/env python3
""" Async basics in Python task 1 """
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int = 0, max_delay: int = 10) -> List[float]:
    """
    async function that calls wait_random n times
    """
    randomDelayList: List[float] = []
    for a in range(n):
        randomDelayList.append(await wait_random(max_delay))
    return sorted(randomDelayList)
