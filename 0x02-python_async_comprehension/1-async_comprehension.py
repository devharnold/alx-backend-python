#!/usr/bin/env python3
'''
using asyncio module with comprehension
'''
from typing import List
from importlib import import_module as using

async_generator = using('0-async_generator').async_generator


async def async_cmprehension() -> List[float]:
    '''
    generates a list of 10 numbers 
    returns a listof 10 numbers
    '''
    random_numbers = [num async for num in async_generator()]
    return random_numbers
