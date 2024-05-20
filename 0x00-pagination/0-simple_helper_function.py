#!/usr/bin/env python3
from typing import Tuple
"""
returns a tuple of size two
"""


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """takes two integer arguments page and page_size returns tuple"""
    start_index: int = (page - 1) * page_size
    return (start_index, start_index + page_size)
