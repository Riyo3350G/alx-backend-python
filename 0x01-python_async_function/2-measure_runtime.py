#!/usr/bin/env python3
""" Async basics in Python task 2 """
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    coroutine that measures the total execution time
    """
    startTime: float = time.time()
    asyncio.run(wait_n(n, max_delay))
    endTime: float = time.time()
    totalTime: float = (endTime - startTime) / n
    return totalTime
