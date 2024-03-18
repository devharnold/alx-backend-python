#!/usr/bin/env python3

import asyncio
from random_delay import wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    delays = []
    tasks = [wait_random(max_delay) for _ in range(n)]

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays