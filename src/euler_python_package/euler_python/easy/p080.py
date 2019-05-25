
from euler_python.utils import eulerlib


def problem080():
    """


    It is well known that if the square root of a natural number is not an
       integer, then it is irrational. The decimal expansion of such square roots
       is infinite without any repeating pattern at all.

       The square root of two is 1.41421356237309504880..., and the digital sum
       of the first one hundred decimal digits is 475.

       For the first one hundred natural numbers, find the total of the digital
       sums of the first one hundred decimal digits for all the irrational square
       roots.
    """
    digits = 100
    multiplier = 100 ** digits
    ans = sum(
        sum(int(c) for c in str(eulerlib.sqrt(i * multiplier))[: digits])
        for i in range(100)
        if eulerlib.sqrt(i) ** 2 != i)
    return ans


if __name__ == "__main__":
    print(problem080())
