#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by position"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """ Deletion-resilient pagination """

        assert isinstance(index, int) and index >= 0
        assert isinstance(page_size, int) and page_size > 0

        data = self.indexed_dataset()

        if index not in data:
            raise AssertionError

        result = []
        current_index = index
        count = 0

        # نجمع page_size عناصر مع تجاهل المحذوف
        while count < page_size and current_index in data:
            result.append(data[current_index])
            current_index += 1
            count += 1

        # نحسب next_index (أول index موجود بعد الصفحة)
        next_index = current_index
        while next_index not in data and next_index < max(data.keys()) + 1:
            next_index += 1

        return {
            "index": index,
            "data": result,
            "page_size": len(result),
            "next_index": next_index if next_index in data else None
        }
