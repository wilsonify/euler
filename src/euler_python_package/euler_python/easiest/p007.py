import itertools

from euler_python.utils import eulerlib


def problem007():
    """
    Computers are fast, so we can implement this solution by testing each number
    individually for primeness, instead of using the more efficient sieve of Eratosthenes.
    The algorithm starts with an infinite stream of incrementing integers starting at 2,
    filters them to keep only the prime numbers, drops the first 10000 items,
    and finally returns the first item thereafter.

    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

    What is the 10001st prime number?
    """

    ans = next(itertools.islice(filter(eulerlib.is_prime, itertools.count(2)), 10000, None))
    return ans


if __name__ == "__main__":
    print(problem007())
