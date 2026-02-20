#!/usr/bin/env python3
"""Type-checked zoom_array function."""

from typing import Tuple, List, Any

def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Return a zoomed-in list by repeating each element factor times."""
    zoomed_in: List = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in
