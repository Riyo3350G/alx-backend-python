#!/usr/bin/env python3
"""Async Generator Module"""
import asyncio
import random


async def async_generator() -> float:
    ''''Async Generator that yields random numbers between 0 and 10'''
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
