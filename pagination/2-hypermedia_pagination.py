#!/usr/bin/env python3
'''Module 1 - simple_pagination'''
from typing import List, Tuple, Dict
import math
import csv


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    ''' Function 0-index_range '''
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        ''' Function 1 - get_page '''
        assert type(page) == int
        assert type(page_size) == int
        assert page > 0 and page_size > 0

        start_index, end_index = index_range(page, page_size)
        return self.dataset()[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        ''' function Hypermedia_pagination '''
        data = self.get_page(page, page_size)

        total_pages = math.ceil(len(self.dataset()) / page_size)

        next_page = page + 1 if page < total_pages else None

        prev_page = page - 1 if page > 1 else None

        hyper_dict = {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }

        return hyper_dict
