#!/usr/bin/env python3

"""
0. Simple helper function
"""


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """
    return a tuple (start, end)
    """
    if isinstance(page_size, int) != int or isinstance(page, int):
        raise TypeError
    return ((page - 1) * page_size, page * page_size)
