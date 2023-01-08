import numpy as np
from math import floor


def is_multiple(n, m):
    """ Determines if a number is a multiple of m """
    return n % m == 0


def is_prime(n):
    """ Determines if a number is prime """
    for i in range(2, floor(np.sqrt(n))+1):  # only need to check up to sqrt(n)
        if n % i == 0:
            return False
    return True


def get_factors(n):
    """
    Computes all factors of a number
    Args:
        n (int): the number to find the factors of

    Returns:
        List of all factors on n (including n and 1)
    """
    all_factors = [1, n]  # initialize with 1 and n
    for i in range(2, floor(np.sqrt(n))+1):
        if n % i == 0:
            all_factors.append(i)
            if i**2 != n:
                all_factors.append(n//i)
    return all_factors
