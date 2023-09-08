#!/usr/bin/env python3
"""
Pagination hypermédia résiliente à la suppression
"""

import csv
import math
from typing import List, Dict


class Server:
    """
    Classe Server pour paginer une base de données
    de noms de bébés populaires.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Données mises en cache
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
            # Ignorer l'en-tête

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Données indexées par position de tri, en commençant à 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            # Tronquer le dataset pour l'exemple
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        ''' function get index with two integer arguments:
        index = None default value
        page_size = 10. '''
        total_items = len(self.indexed_dataset())

        if index is not None and index not in self.indexed_dataset():
            next_index = index + 1
            while next_index < total_items and \
                    next_index not in self.indexed_dataset():
                next_index += 1
            start_index = next_index
        else:
            start_index = index if index is not None else 0

        end_index = min(start_index + page_size, total_items)

        data = [self.indexed_dataset()[i] for i in range(
            start_index, end_index)]

        next_index = end_index if end_index < total_items else None

        result = {
            'index': start_index,
            'next_index': next_index,
            'page_size': page_size,
            'data': data,
        }

        return result
