#!/usr/bin/env python3
from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Computes the length of each element in an iterable of sequences.

    This function takes an iterable of sequences and returns a list of tuples,
    where each tuple contains a sequence and its length.

    Parameters:
    lst (Iterable[Sequence]): An iterable of sequences (e.g., lists, strings, etc.).

    Returns:
    List[Tuple[Sequence, int]]: A list of tuples, each containing a sequence from `lst`
                                 and its corresponding length.
    """
    return [(i, len(i)) for i in lst]
