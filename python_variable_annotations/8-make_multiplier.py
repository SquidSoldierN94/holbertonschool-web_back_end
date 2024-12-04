#!/usr/bin/env python3
from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates a multiplier function.

    This function takes a float `multiplier` and returns a new function that 
    multiplies any given float by the `multiplier`.

    Parameters:
    multiplier (float): The number by which the returned function will multiply.

    Returns:
    Callable[[float], float]: A function that takes a float as input and 
                               returns the result of multiplying it by `multiplier`.
    """
    def multiplier_function(n: float) -> float:
        return n * multiplier
    return multiplier_function
