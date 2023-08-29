#!/usr/bin/env python3
''' Module 8 - element_length '''
from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    ''' Function 9-element_length '''
    return [(i, len(i)) for i in lst]
