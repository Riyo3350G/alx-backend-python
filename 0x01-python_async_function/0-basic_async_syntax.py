#!/usr/bin/env python3
""" Async basics in Python task 0 """
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    async function that waits for a random delay between 0 and max_delay
    """
    randomDelay = random.uniform(0, max_delay)
    await asyncio.sleep(randomDelay)
    return randomDelay
