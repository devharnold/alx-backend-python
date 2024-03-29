#!/usr/bin/env python3
"""using asyncio module with comprehension"""
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """generates a list of 10 numbers 
    returns a list of 10 numbers
    comprehension 
    then return the 10 random numbers"""
    return [num async for num in async_generator()]