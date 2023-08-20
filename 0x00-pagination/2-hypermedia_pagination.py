#!/usr/bin/env python3

"""Pagination with hypermedia."""
from typing import Tuple

import csv
import math
from typing import List, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """return start and end index."""
    end = page * page_size
    start = end - page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get page using index_range to know the start and stop index."""
        assert (type(page) == int)
        assert (type(page_size) == int)
        assert (page > 0 and page_size > 0)
        assert (page > 0 and page_size > 0)

        start, stop = index_range(page, page_size)
        return self.dataset()[start: stop]

    def get_hyper(self, page: int = 1, page_size: int = 10) \
            -> Dict:
        """get_page with info for the next and previous"""
        return {
            "page_size": page_size,
            "page": page,
            "data": self.get_page(page, page_size),
            "next_page": page + 1,
            "prev_page": None if page - 1 < 1 else page - 1,
            "total_pages": math.ceil(len(self.dataset()) / page_size),
        }
