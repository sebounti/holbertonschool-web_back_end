#!/usr/bin/env python3
''' Module 0 - async_generator '''

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None, None]:
    ''' Function 0 - async_generator'''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
