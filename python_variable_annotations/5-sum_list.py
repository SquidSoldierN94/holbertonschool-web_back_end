#!/usr/bin/env python3
from typing import List

def sum_list(input_list: List[float]) -> float:
    """
    Sums all the elements in a list of floats.

    This function takes a list of floating-point numbers and returns their sum.

    Parameters:
    input_list (List[float]): A list of float numbers to sum.

    Returns:
    float: The sum of all the numbers in the input list.
    """
    return sum(input_list)
