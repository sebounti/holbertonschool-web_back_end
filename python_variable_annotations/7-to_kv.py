#!/usr/bin/env python3
'''' Module 7 - to_kv '''
import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    ''' Function 7-to_kv '''
    return k, v ** 2
