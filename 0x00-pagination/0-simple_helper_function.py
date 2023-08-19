#!/usr/bin/env python3

"""Paginate."""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """return start and end index."""
    end = page * page_size
    start = end - page_size
    return (start, end)
