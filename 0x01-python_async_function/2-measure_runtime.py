#!/usr/bin/env python3
""" Async basics in Python task 2 """
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int = 0, max_delay: int = 10) -> float:
    """
    coroutine that measures the total execution time
    """
    startTime = time.time()
    asyncio.run(wait_n(n, max_delay))
    endTime = time.time()
    totalTime = endTime - startTime
    return totalTime / n
