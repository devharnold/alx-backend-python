#!/usr/bin/env python3
'''handles complex-types functions'''
from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''returns a func; multiplies float by multiplier'''
    def multiplier_func(i: float) -> float:
        return i * multiplier
    return multiplier_func