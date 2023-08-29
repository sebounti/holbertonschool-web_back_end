#!/usr/bin/env python3
''' Module 6 - sum_mixed_list '''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    ''' Function 5-sum_mixed_list '''
    return [i + j for i, j in zip(mxd_lst)]
