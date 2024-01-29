#!/usr/bin/env python3
"""
0. Simple helper function
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    return in a list for those particular pagination parameters
    """
    if isinstance(page_size, int) != int or isinstance(page, int):
        raise TypeError
    return ((page - 1) * page_size, page * page_size)
