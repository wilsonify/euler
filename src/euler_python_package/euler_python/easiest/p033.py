import math


def problem033():
    """


    The fraction 49/98 is a curious fraction, as an inexperienced
       mathematician in attempting to simplify it may incorrectly believe that
       49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

       We shall consider fractions like, 30/50 = 3/5, to be trivial
       examples.

       There are exactly four non-trivial examples of this type of fraction, less
       than one in value, and containing two digits in the numerator and
       denominator.

       If the product of these four fractions is given in its lowest common
       terms, find the value of the denominator.


           # Consider an arbitrary fraction n/d:
    #   Let n = 10 * n1 + n0 be the numerator.
    #   Let d = 10 * d1 + d0 be the denominator.
    # As stated in the problem, we need 10 <= n < d < 100.
    # We must disregard trivial simplifications where n0 = d0 = 0.
    # Now, a     simplification     with n0 = d0 is impossible because:
    # n1 / d1 = n / d = (10*n1 + n0) / (10*d1 + n0).
    #   n1 * (10*d1 + n0) = d1 * (10*n1 + n0).
    #   10*n1*d1 + n1*n0 = 10*d1*n1 + d1*n0.
    #   n1*n0 = d1*n0.
    #   n1 = d1.
    #   This implies n = d, which contradicts the fact that n < d.
    # Similarly, we cannot have a simplification with n1 = d1 for the same reason.
    # Therefore we only need to consider the cases where n0 = d1 or n1 = d0.
    # In the first case, check that n1/d0 = n/d;
    # in the second case, check that n0/d1 = n/d.

    """
    numer = 1
    denom = 1
    for d in range(10, 100):
        for n in range(10, d):
            n0 = n % 10
            n1 = n // 10
            d0 = d % 10
            d1 = d // 10
            if (n1 == d0 and n0 * d == n * d1) or (n0 == d1 and n1 * d == n * d0):
                numer *= n
                denom *= d
    return denom // math.gcd(numer, denom)


if __name__ == "__main__":
    print(problem033())
