from euler_python.utils import eulerlib


def problem087():
    """


    The smallest number expressible as the sum of a prime square, prime cube,
       and prime fourth power is 28. In fact, there are exactly four numbers
       below fifty that can be expressed in such a way:

       28 = 2^2 + 2^3 + 2^4
       33 = 3^2 + 2^3 + 2^4
       49 = 5^2 + 2^3 + 2^4
       47 = 2^2 + 3^3 + 2^4

       How many numbers below fifty million can be expressed as the sum of a
       prime square, prime cube, and prime fourth power?
    """
    limit = 50000000
    primes = eulerlib.list_primes(eulerlib.sqrt(limit))

    sums = {0}
    for i in range(2, 5):
        newsums = set()
        for p in primes:
            q = p ** i
            if q > limit:
                break
            for x in sums:
                if x + q <= limit:
                    newsums.add(x + q)
        sums = newsums
    return len(sums)


if __name__ == "__main__":
    print(problem087())
