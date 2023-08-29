#!/usr/bin/env python3
''' Module 1 - concat '''
import asyncio
from typing import List

wait_random = __import__('3-tasks').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    ''' Function 1 - wait_n '''
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
