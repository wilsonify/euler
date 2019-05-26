#
#
import sys

from euler_python.utils import eulerlib


# We compute the Collatz chain length for every integer in the range according to the iteration rule.
# Also, we cache the Collatz value for all integer arguments to speed up the computation.
def problem014():
    """
    The following iterative sequence is defined for the set of positive
       integers:

       n → n/2 (n is even)
       n → 3n + 1 (n is odd)

       Using the rule above and starting with 13, we generate the following
       sequence:

                       13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

       It can be seen that this sequence (starting at 13 and finishing at 1)
       contains 10 terms. Although it has not been proved yet (Collatz Problem),
       it is thought that all starting numbers finish at 1.

       Which starting number, under one million, produces the longest chain?

       NOTE: Once the chain starts the terms are allowed to go above one million.
    """

    sys.setrecursionlimit(3000)
    ans = max(range(1, 1000000), key=collatz_chain_length)
    return ans


@eulerlib.Memoize
def collatz_chain_length(x):
    if x == 1:
        return 1
    if x % 2 == 0:
        y = x // 2
    else:
        y = x * 3 + 1
    return collatz_chain_length(y) + 1


if __name__ == "__main__":
    print(problem014())
