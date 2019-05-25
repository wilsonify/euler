from euler_python.utils import eulerlib


def smallest_prime_factor(n):
    """
    :param n:
    :return: the smallest factor of n, which is in the range [2, n]. The result is always prime.
    """
    assert n >= 2
    for i in range(2, eulerlib.sqrt(n) + 1):
        if n % i == 0:
            return i
    return n  # n itself is prime


def largest_prime_factor(n):
    """
    By the fundamental theorem of arithmetic,
    every integer n > 1 has a unique factorization as a product of prime numbers.

    In other words, the theorem says that n = p_0 * p_1 * ... * p_{m-1},
    where each p_i > 1 is prime but not necessarily unique.

    Now if we take the number n and repeatedly divide out its smallest factor (which must also be prime),
    then the last factor that we divide out must be the largest prime factor of n.
    For reference, 600851475143 = 71 * 839 * 1471 * 6857.

    :param n:
    :return:
    """
    while True:
        p = smallest_prime_factor(n)
        if p < n:
            n //= p
        else:
            return n


def problem003():
    """
    The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600851475143 ?
    """

    return largest_prime_factor(600851475143)


if __name__ == "__main__":
    print(problem003())
