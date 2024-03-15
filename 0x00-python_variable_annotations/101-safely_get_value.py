#!/usr/bin/env python3
from typing import TypeVar, Dict, Any, Optional

K = TypeVar('K')
V = TypeVar('V')

def safely_get_value(dct: Dict[K, V], key: K, default: Optional[V] = None) -> Optional[V]:
    """Get value associated with key from the dict safely"""
    if key in dct:
        return dct[key]
    else:
        return default