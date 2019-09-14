import itertools

from euler_python.utils import eulerlib


def problem077():
    """


    It is possible to write ten as the sum of primes in exactly five different
       ways:

       7 + 3
       5 + 5
       5 + 3 + 2
       3 + 3 + 2 + 2
       2 + 2 + 2 + 2 + 2

       What is the first value which can be written as the sum of primes in over
       five thousand different ways?
    """

    cond = lambda n: num_prime_sum_ways(n) > 5000
    ans = next(filter(cond, itertools.count(2)))
    return ans


primes = [2]


def num_prime_sum_ways(n):
    for i in range(primes[-1] + 1, n + 1):
        if eulerlib.is_prime(i):
            primes.append(i)

    ways = [1] + [0] * n
    for p in primes:
        for i in range(n + 1 - p):
            ways[i + p] += ways[i]
    return ways[n]


if __name__ == "__main__":
    print(problem077())
