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
        assert index is None or 0 <= index < len(self.indexed_dataset())
        assert type(page_size) == int and page_size > 0

        current_index = index if index is not None else 0
        next_index = current_index + page_size

        indexed_data = self.indexed_dataset()
        data = []

        i = current_index
        while i < next_index and i < len(indexed_data):
            data.append(indexed_data.get(i, []))
            i += 1

        return {
            "index": current_index,
            "data": data,
            "page_size": page_size,
            "next_index": next_index
        }
