#!/usr/bin/env python3
''' Module 6 - sum_mixed_list '''
import math


def sum_mixed_list(list_1: list, list_2: list) -> list:
    ''' Function 5-sum_list '''
    return [i + j for i, j in zip(list_1, list_2)]
