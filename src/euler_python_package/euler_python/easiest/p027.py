"""
Problem 27

Euler discovered the remarkable quadratic formula:

                                  n² + n + 41

   It turns out that the formula will produce 40 primes for the consecutive
   values n = 0 to 39. However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41
   is divisible by 41, and certainly when n = 41, 41² + 41 + 41 is clearly
   divisible by 41.

   The incredible formula  n² − 79n + 1601 was discovered, which produces 80
   primes for the consecutive values n = 0 to 79. The product of the
   coefficients, −79 and 1601, is −126479.

   Considering quadratics of the form:

     n² + an + b, where |a| < 1000 and |b| < 1000

     where |n| is the modulus/absolute value of n
     e.g. |11| = 11 and |−4| = 4

   Find the product of the coefficients, a and b, for the quadratic
   expression that produces the maximum number of primes for consecutive
   values of n, starting with n = 0.
"""

import itertools

from euler_python.utils import eulerlib


def count_consecutive_primes(a_b):
    """
    count_consecutive_primes for use a key=count_consecutive_primes
    :param a_b: tuple (a,b)
    :return: i
    """
    input_a, input_b = a_b
    i = 0
    for i in itertools.count():
        intermediate_n = i * i + i * input_a + input_b
        if not is_prime(intermediate_n):
            break
    return i


IS_PRIME_CACHE = eulerlib.list_primality(1000)


def is_prime(input_n):
    """
    cached version of eulerlib.is_prime
    :param input_n:
    :return:
    """
    if input_n < 0:
        return False
    if input_n < len(IS_PRIME_CACHE):
        return IS_PRIME_CACHE[input_n]
    return eulerlib.is_prime(input_n)


def product_of_coefficients(limit=1000):
    """
        Euler discovered the remarkable quadratic formula:

                                      n² + n + 41

       It turns out that the formula will produce 40 primes for the consecutive
       values n = 0 to 39. However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41
       is divisible by 41, and certainly when n = 41, 41² + 41 + 41 is clearly
       divisible by 41.

       The incredible formula  n² − 79n + 1601 was discovered, which produces 80
       primes for the consecutive values n = 0 to 79. The product of the
       coefficients, −79 and 1601, is −126479.

       Considering quadratics of the form:

         n² + an + b, where |a| < 1000 and |b| < 1000

         where |n| is the modulus/absolute value of n
         e.g. |11| = 11 and |−4| = 4


    """

    ans = max(((a, b) for a in range(-(limit - 1), limit) for b in range(2, limit)),
              key=count_consecutive_primes)
    return ans[0] * ans[1]


def problem027():
    """
    Find the product of the coefficients, a and b,
    for the quadratic expression
    that produces the maximum number of primes
    for consecutive values of n, starting with n = 0.
    :return:
    """
    return product_of_coefficients()


if __name__ == "__main__":
    print(problem027())
