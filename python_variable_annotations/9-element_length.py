#!/usr/bin/env python3

"""
This module contains the function `element_length` which computes the length
of each element in an iterable of sequences. It demonstrates the use of type
annotations, iterables, and sequences.
"""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:

    """
    Computes the length of each element in an iterable of sequences.

    This function takes an iterable of sequences and returns a list of tuples,
    where each tuple contains a sequence and its length.

    Parameters:
    lst (Iterable[Sequence]) (e.g., lists, strings, etc.).

    Returns:
    List[Tuple[Sequence, int]] a sequence from `lst`
                                 and its corresponding length.
    """
    return [(i, len(i)) for i in lst]
