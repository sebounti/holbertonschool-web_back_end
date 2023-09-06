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
        """
        Obtenir une page de données avec index
        hypermédia résiliente à la suppression
        """

        data = self.dataset()
        # Obtenir les données réelles

        # Vérifier si l'index fourni est valide
        assert index is None or (index >= 0 and index < len(data))

        if index is None:
            # Si l'index est None, le définir sur 0 (début depuis le début)
            index = 0
        else:
            # Si un index est fourni, l'ajuster pour le début de la nexte page
            index = (index // page_size) * page_size + page_size

        next_index = index + page_size
        # Calculer l'index suivant à interroger

        data = self.dataset()[index:next_index]
        # Obtenir la page réelle de données

        hyper_dict = {
            'index': index,
            'next_index': next_index,
            'page_size': page_size,
            'data': data
        }

        return hyper_dict
