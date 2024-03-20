#!/usr/bin/env python3
"""
using asyncio module
"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Executes async_comprehension 4 times and measure the
    total execution time
    """
    start_time = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(), async_comprehension(), async_comprehension())
    return (time.perf_counter() - start_time)