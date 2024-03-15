#!/usr/bin/env python3
"""Handles a mixed list"""
from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """returns the sum of mixed list"""
    return float(sum(mxd_lst))