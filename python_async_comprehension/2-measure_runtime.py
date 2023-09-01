#!/usr/bin/env python3
"""Module 2 - measure_runtime"""
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Function 2 - measure_runtime"""
    start_time = time.time()
    tasks = [async_comprehension() for _ in range(4)]
    results = await asyncio.gather(*tasks)
    end_time = time.time()
    total_time = end_time - start_time
    return total_time
