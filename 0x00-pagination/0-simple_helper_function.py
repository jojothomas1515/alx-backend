#!/usr/bin/env python3

"""Paginate."""
from typing import Tuple


def index_range(page: int, pageSize: int) -> Tuple(int, int):
    """return start and end index."""
    end = page * pageSize
    start = end - pageSize
    return (start, end)
