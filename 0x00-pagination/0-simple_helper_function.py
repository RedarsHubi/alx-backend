#!/usr/bin/env python3
"""
returns a tuple of size two
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """takes two integer arguments page and page_size returns tuple"""
    return ((page - 1) * page_size, page_size * page)
