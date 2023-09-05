#!/usr/bin/env python3
'''module 0-simple_helper_function'''
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    ''' Function 0-index_range '''
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)
