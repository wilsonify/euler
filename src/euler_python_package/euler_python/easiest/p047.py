#
# 
#
#
import itertools

from euler_python.utils import eulerlib


def problem047():
    """


    The first two consecutive numbers to have two distinct prime factors are:

       14 = 2 × 7
       15 = 3 × 5

       The first three consecutive numbers to have three distinct prime factors
       are:

       644 = 2² × 7 × 23
       645 = 3 × 5 × 43
       646 = 2 × 17 × 19.

       Find the first four consecutive integers to have four distinct prime
       factors. What is the first of these numbers?
    """

    def cond(i):
        return all((count_distinct_prime_factors(i + j) == 4) for j in range(4))

    ans = next(filter(cond, itertools.count()))
    return ans


@eulerlib.memoize
def count_distinct_prime_factors(n):
    count = 0
    while n > 1:
        count += 1
        for i in range(2, eulerlib.sqrt(n) + 1):
            if n % i == 0:
                while True:
                    n //= i
                    if n % i != 0:
                        break
                break
        else:
            break  # n is prime
    return count


if __name__ == "__main__":
    print(problem047())
