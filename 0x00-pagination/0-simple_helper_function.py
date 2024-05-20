#!/usr/bin/env python3
from typing import Tuple
"""
returns a tuple of size two
"""


def index_range(page: int, page_size: int) -> Tuple:
    """takes two integer arguments page and page_size returns tuple"""
    return ((page - 1) * page_size, page_size * page)
