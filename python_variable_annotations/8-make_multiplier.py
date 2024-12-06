#!/usr/bin/env python3

"""
This module contains which generates a new function
that multiplies any. It demonstrates the
use of higher-order functions, closures, and type annotations.
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:

    """
    Creates a multiplier function.

    This and returns a new function that
    multiplies any given float by the `multiplier`.

    Parameters:
    multiplier the returned function will multiply.

    Returns:
    Callable[[float], float]: as input and
    returns the result of multiplying it by `multiplier`.
    """
    def multiplier_function(n: float) -> float:
        return n * multiplier
    return multiplier_function
