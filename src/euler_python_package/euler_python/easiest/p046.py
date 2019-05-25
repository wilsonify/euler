import itertools

from euler_python.utils import eulerlib


def problem046():
    """


    It was proposed by Christian Goldbach that every odd composite number can
       be written as the sum of a prime and twice a square.

       9 = 7 + 2×1^2
       15 = 7 + 2×2^2
       21 = 3 + 2×3^2
       25 = 7 + 2×3^2
       27 = 19 + 2×2^2
       33 = 31 + 2×1^2

       It turns out that the conjecture was false.

       What is the smallest odd composite that cannot be written as the sum of a
       prime and twice a square?
    """
    ans = next(itertools.filterfalse(test_goldbach, itertools.count(9, 2)))
    return ans


def test_goldbach(n):
    if n % 2 == 0 or eulerlib.is_prime(n):
        return True
    for i in itertools.count(1):
        k = n - 2 * i * i
        if k <= 0:
            return False
        elif eulerlib.is_prime(k):
            return True


if __name__ == "__main__":
    print(problem046())
