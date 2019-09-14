from euler_python.utils import eulerlib


def problem053():
    """


    There are exactly ten ways of selecting three from five, 12345:

                  123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

       In combinatorics, we use the notation, ^5C[3] = 10.

       In general,

          ^nC[r] =    n!    ,where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.
                   r!(n−r)!

       It is not until n = 23, that a value exceeds one-million: ^23C[10] =
       1144066.

       How many, not necessarily distinct, values of  ^nC[r], for 1 ≤ n ≤ 100,
       are greater than one-million?
    """

    ans = sum(
        1
        for n in range(1, 101)
        for k in range(0, n + 1)
        if eulerlib.binomial(n, k) > 1000000
    )
    return ans


if __name__ == "__main__":
    print(problem053())
