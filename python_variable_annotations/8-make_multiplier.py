#!/usr/bin/env python3
''' Module 8-make_multiplier '''
import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    ''' Function 8-make_multiplier '''
    return lambda x: x * multiplier
