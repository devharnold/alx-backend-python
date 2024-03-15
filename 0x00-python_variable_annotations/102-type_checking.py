#!/usr/bin/env python3
from typing import Tuple, Any, List

def zoom_array(lst: Tuple[Any, ...], factor: int = 2) -> Tuple[Any, ...]:
    '''advanced duck typing using python'''
    zoomed_in = List[Any] = [
        item for item in lst
        for i in range(factor)
    ]
    return tuple(zoomed_in)

array = (12, 79, 91)
zoom_2x = zoom_array(array)
zoom_3x = zoom_array(array, 3)