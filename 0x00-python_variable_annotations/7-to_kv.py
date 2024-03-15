#!/usr/bin/env python3
'''handles complex types'''
from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''converts a str key and int or float into a tuple'''
    return k, float(v) ** 2