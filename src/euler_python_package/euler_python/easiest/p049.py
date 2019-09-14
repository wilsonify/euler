from euler_python.utils import eulerlib


def problem049():
    """
    The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
    increases by 3330, is unusual in two ways: (i) each of the three terms are
    prime, and, (ii) each of the 4-digit numbers are permutations of one another.
    There are no arithmetic sequences made up of three 1-, 2-, or 3-digit
    primes, exhibiting this property, but there is one other 4-digit
    increasing sequence.

    What 12-digit number do you form by concatenating the three terms in this
    sequence?
"""

    limit = 10000
    isprime = eulerlib.list_primality(limit - 1)
    for base in range(1000, limit):
        if isprime[base]:
            for step in range(1, limit):
                a = base + step
                b = a + step
                if (
                        a < limit
                        and isprime[a]
                        and has_same_digits(a, base)
                        and b < limit
                        and isprime[b]
                        and has_same_digits(b, base)
                        and (base != 1487 or a != 4817)
                ):
                    return int(str(base) + str(a) + str(b))
    raise RuntimeError("Not found")


def has_same_digits(x, y):
    return sorted(str(x)) == sorted(str(y))


if __name__ == "__main__":
    print(problem049())
