#!/usr/bin/env python3

'''
Using the asyncio module to generate and execyte tasks
'''
import asyncio
import time

'''Import wait_n from the prev file'''
wait_n = __import__('1-concurrent_coroutines').wait_n

def measure_time(n: int, max_delay: int) -> float:
    '''
    Function that measures the total execution time for `wait_n`
    and returns the `total_time / n`
    Attributes:
        n: number of times to execute `wait_n`
        max_delay: maximum delay of each execution of `wait_random`
    Function should return a float
    '''
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - start_time) / n