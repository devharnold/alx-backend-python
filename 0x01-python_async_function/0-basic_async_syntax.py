#!/usr/bin/python3

import os
import asyncio
import random

async def wait_random(max_delay: int) -> int:
    max_delay = 10
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay







 #async def wait_n(n, max_delay: int):
 #   delay = max_delay / n
 #   tasks = []
 #   for i in range(n):
 #       tasks.append(asyncio.create_task(asyncio.sleep(delay)))
 #       for task in tasks:
 #           await task
 #           print(delay)
 #   
 #   return tasks