"""
library of utilities
"""
import array
import math


def popcount(input_x):
    """
    Hamming weight

    :param input_x: non-negative integer
    :return: the number of 1's in the binary representation of x
    """
    return bin(input_x).count("1")


def sqrt(input_x):
    """
    Given integer x, this returns the integer floor(sqrt(x)).
    :param input_x:
    :return:
    """
    assert input_x >= 0
    i = 1
    while i * i <= input_x:
        i *= 2
    intermediate_y = 0
    while i > 0:
        if (intermediate_y + i) ** 2 <= input_x:
            intermediate_y += i
        i //= 2
    return intermediate_y


def is_square(input_x):
    """
    # Tests whether x is a perfect square, for any integer x.
    :param input_x:
    :return:
    """
    if input_x < 0:
        return False
    intermediate_y = sqrt(input_x)
    return intermediate_y * intermediate_y == input_x


def is_prime(input_x):
    """
    # Tests whether the given integer is a prime number.
    :param input_x:
    :return:
    """
    if input_x <= 1:
        return False
    if input_x <= 3:
        return True
    if input_x % 2 == 0:
        return False
    for i in range(3, sqrt(input_x) + 1, 2):
        if input_x % i == 0:
            return False
    return True


def list_primality(input_n):
    """
    Sieve of Eratosthenes

    For 0 <= i <= n, result[i] is True if i is a prime number, False otherwise.

    :param input_n: int
    :return: a list of True and False indicating whether each number is prime.
    """
    result = [True] * (input_n + 1)
    result[0] = result[1] = False
    for i in range(sqrt(input_n) + 1):
        if result[i]:
            for j in range(i * i, len(result), i):
                result[j] = False
    return result


def list_primes(input_n):
    """
    # Returns all the prime numbers less than or equal to n, in ascending order.
    # For example: listPrimes(97) = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, ..., 83, 89, 97].

    :param input_n:
    :return:
    """
    return [i for (i, isprime) in enumerate(list_primality(input_n)) if isprime]


def prime_generator(limit):
    """
    # Yields prime numbers in ascending order from 2 to limit (inclusive).
    :param limit:
    :return:
    """
    if limit >= 2:
        yield 2

    # Sieve of Eratosthenes, storing only odd numbers starting at 3
    isprime = array.array("B", b"\x01" * ((limit - 1) // 2))
    sieveend = sqrt(limit)
    for i, _ in enumerate(isprime):
        if isprime[i] == 1:
            prime_p = i * 2 + 3
            yield prime_p
            if i <= sieveend:
                for j in range((prime_p * prime_p - 3) >> 1, len(isprime), prime_p):
                    isprime[j] = 0


def list_smallest_prime_factors(input_n):
    """

    :param input_n:
    :return:
    """
    result = [None] * (input_n + 1)
    limit = sqrt(input_n)
    for i in range(2, len(result)):
        if result[i] is None:
            result[i] = i
            if i <= limit:
                for j in range(i * i, input_n + 1, i):
                    if result[j] is None:
                        result[j] = i
    return result


def list_totients(input_n):
    """

    :param input_n:
    :return:
    """
    result = list(range(input_n + 1))
    for i in range(2, len(result)):
        if result[i] == i:  # i is prime
            for j in range(i, len(result), i):
                result[j] -= result[j] // i
    return result


def binomial(input_n, input_k):
    """

    :param input_n:
    :param input_k:
    :return:
    """
    assert 0 <= input_k <= input_n
    return math.factorial(input_n) // (
            math.factorial(input_k) * math.factorial(input_n - input_k)
    )


# Returns x^-1 mod m. Note that x * x^-1 mod m = x^-1 * x mod m = 1.
def reciprocal_mod(input_x, input_m):
    """
    # Based on a simplification of the extended Euclidean algorithm

    :param input_x:
    :param input_m:
    :return:
    """
    assert 0 <= input_x < input_m

    intermediate_y = input_x
    input_x = input_m
    intermediate_a = 0
    intermediate_b = 1
    while intermediate_y != 0:
        intermediate_a, intermediate_b = (
            intermediate_b,
            intermediate_a - input_x // intermediate_y * intermediate_b,
        )
        input_x, intermediate_y = intermediate_y, input_x % intermediate_y
    if input_x == 1:
        return intermediate_a % input_m
    raise ValueError("Reciprocal does not exist")


def next_permutation(arr):
    """
    :param arr:
    :return:
    """

    i = len(arr) - 1
    while i > 0 and arr[i - 1] >= arr[i]:
        i -= 1
    if i <= 0:
        return False

    # Find successor to pivot
    j = len(arr) - 1
    while arr[j] <= arr[i - 1]:
        j -= 1
    arr[i - 1], arr[j] = arr[j], arr[i - 1]

    # Reverse suffix
    arr[i:] = arr[len(arr) - 1: i - 1: -1]
    return True


class Memoize:
    """
    # Decorator.
    """

    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args, **kwargs):
        if args in self.cache:
            return self.cache[args]
        val = self.func(*args, **kwargs)
        self.cache[args] = val
        return val

    def get_cache(self):
        """
        access method
        :return:
        """
        return self.cache
