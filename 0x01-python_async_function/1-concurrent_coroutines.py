#!/usr/bin/env python3
'''
Using the asyncio to execute tasks
'''
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Executes the wait_random and returns the list of all the delays(float values)
    The list should be in ascending order without using `sort()`
    Attributes: 
        n: number of times taken to execute wait_random
        max_delay: maximum delay of each execution of wait_random
    '''
    wait_times = asyncio.gather(*[wait_random(max_delay) for _ in range(n)])
    return sorted(await wait_times)
