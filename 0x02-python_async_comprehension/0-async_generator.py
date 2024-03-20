#!/usr/bin/env python3
'''
Async comprehension module
'''
import asyncio
import random
from typing import Generator


async def async_generator():
    '''
    function that will loop 10 times 
    each asynchronously wait for 1 second then yield a random
    number between 0 and 10 
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)