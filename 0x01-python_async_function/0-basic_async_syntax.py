#!/usr/bin/python3

import os
import asyncio
import random


async def wait_n(n, max_delay: int):
    delay = max_delay / n
    tasks = []
    for i in range(n):
        tasks.append(asyncio.create_task(asyncio.sleep(delay)))
        for task in tasks:
            await task
            print(delay)
    
    return tasks