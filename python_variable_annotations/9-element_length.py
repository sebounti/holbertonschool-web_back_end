#!/usr/bin/env python3
''' Module 8 - element_length '''
import typing


def element_length(lst: typing.Iterable[typing.Sequence]) -> \
    typing.List[typing.Tuple[typing.Sequence, int]]:
    ''' Function 9-element_length '''
    return [(i, len(i)) for i in lst]
