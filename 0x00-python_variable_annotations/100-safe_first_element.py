#!/usr/bin/env python3
"""handles duck typing"""
from typing import List, Optional, TypeVar
T = TypeVar('T')

def safe_first_element(lst: List[T]) -> Optional[T]:
    """first element of a sequence"""
    if lst:
        return lst[0]
    else:
        return None