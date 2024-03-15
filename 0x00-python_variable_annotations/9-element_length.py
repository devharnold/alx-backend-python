#!/usr/bin/env python3
'''handles iterable objects(advanced duck typing)'''
from typing import List, Tuple

def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    '''returns values of appropriate types'''
    return [(i, len(i)) for i in lst]