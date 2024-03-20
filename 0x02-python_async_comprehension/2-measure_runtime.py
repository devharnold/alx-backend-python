#!/usr/bin/env python3
"""
using asyncio module
"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    A measure_runtime coroutine that will execute
    async_comprehension four times in parallel using
    asyncio.gather. measure_runtime should measure
    the total runtime and return it.
    """
    start_time = time.time()
    await asyncio.gather(async_comprehension(), async_comprehension(), async_comprehension(), async_comprehension())
    end_time = time.time()
    return end_time - start_time