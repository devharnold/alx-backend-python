#!/usr/bin/env python3

'''
Using the asyncio module to generate tasks
'''
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Executes the wait_random and returns the list of all the delays(float)
    Should be sorted but without using the `sort()` function
    Attributes:
        max_delay: the maximum delay time taken
        wait_times: 
    '''
    wait_times = asyncio.gather(*[task_wait_random(max_delay) for _ in range(n)])
    return sorted(await wait_times)





   # wait_times = await asyncio.gather(
   #     *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
   # )
   # return sorted(wait_times)