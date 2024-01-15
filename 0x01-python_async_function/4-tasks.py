#!/usr/bin/env python3
""" Async basics in Python project, Task 4 """
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    async function that calls task_wait_random n times
    """
    randomDelayList: List[float] = []
    a = max_delay
    [randomDelayList.append(await task_wait_random(a)) for _ in range(n)]
    return sorted(randomDelayList)
