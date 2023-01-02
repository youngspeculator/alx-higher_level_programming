#!/usr/bin/python3
"""A function that prints a square with the character #"""


def print_square(size):
    """Prints a square

    Args:
        size: (int) the length of the square

    Raises:
        TypeError: `size must be an integer` if size is not an integer
        TypeError: `size must be an integer` if size is a float and < 0
        ValueError: `size must be >= 0` if size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >=0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
