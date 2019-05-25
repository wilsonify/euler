#
# 
#
#
import fractions

import math
from euler_python.utils import eulerlib


# Based on this insane theorem: Suppose D > 1 is an integer, non-perfect-square.
# 
# Express sqrt(D) as the continued fraction (a0, a1, ..., a_{n-1}, (b0, b1, ..., b_{m-1})),
# where the sequence of b's is the periodic part.
# 
# Let p/q (in lowest terms) = (a0, a1, ..., a_{n-1}, b0, b1, ..., b_{m-2}).
# (This is a truncation of the continued fraction with only one period minus the last term.)
# 
# Then the minimum solution (x, y) for Pell's equation is given by:
# - (p, q) if m is even
# - (p^2 + D q^2, 2pq) if m is odd
def problem066():
    """


    Consider quadratic Diophantine equations of the form:

                                     x^2 – Dy^2 = 1

       For example, when D=13, the minimal solution in x is 649^2 – 13×180^2 = 1.

       It can be assumed that there are no solutions in positive integers when D
       is square.

       By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the
       following:

       3^2 – 2×2^2 = 1
       2^2 – 3×1^2 = 1
       9^2 – 5×4^2 = 1
       5^2 – 6×2^2 = 1
       8^2 – 7×3^2 = 1

       Hence, by considering minimal solutions in x for D ≤ 7, the largest x is
       obtained when D=5.

       Find the value of D ≤ 1000 in minimal solutions of x for which the largest
       value of x is obtained.
    """
    ans = max((n for n in range(2, 1001) if (not eulerlib.is_square(n))),
              key=smallest_solution_x)
    return ans


# Returns the smallest x such that x > 0 and there exists some y such that x^2 - n y^2 = 1.
# Requires n to not be a perfect square.
def smallest_solution_x(n):
    contfrac = sqrt_to_continued_fraction(n)
    temp = contfrac[0] + contfrac[1][: -1]

    val = fractions.Fraction(temp[-1], 1)
    for term in reversed(temp[: -1]):
        val = 1 / val + term

    if len(contfrac[1]) % 2 == 0:
        return val.numerator
    else:
        return val.numerator ** 2 + val.denominator ** 2 * n


# Returns the periodic continued fraction of sqrt(n). Requires n to not be a perfect square.
# result[0] is the minimal non-periodic prefix, and result[1] is the minimal periodic tail.
def sqrt_to_continued_fraction(n):
    terms = []
    seen = {}
    val = QuadraticSurd(0, 1, 1, n)
    while True:
        seen[val] = len(seen)
        flr = val.floor()
        terms.append(flr)
        val = (val - QuadraticSurd(flr, 0, 1, val.d)).reciprocal()
        if val in seen:
            break
    split = seen[val]
    return (terms[: split], terms[split:])


# Represents (a + b * sqrt(d)) / c. d must not be a perfect square.
class QuadraticSurd(object):

    def __init__(self, a, b, c, d):
        if c == 0:
            raise ValueError()

        # Simplify
        if c < 0:
            a = -a
            b = -b
            c = -c
        gcd = math.gcd(math.gcd(a, b), c)
        if gcd != 1:
            a //= gcd
            b //= gcd
            c //= gcd

        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __sub__(self, other):
        if self.d != other.d:
            raise ValueError()
        return QuadraticSurd(
            self.a * other.c - other.a * self.c,
            self.b * other.c - other.b * self.c,
            self.c * other.c,
            self.d)

    def reciprocal(self):
        return QuadraticSurd(
            -self.a * self.c,
            self.b * self.c,
            self.b * self.b * self.d - self.a * self.a,
            self.d)

    def floor(self):
        temp = eulerlib.sqrt(self.b * self.b * self.d)
        if self.b < 0:
            temp = -(temp + 1)
        temp += self.a
        if temp < 0:
            temp -= self.c - 1
        return temp // self.c

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b \
               and self.c == other.c and self.d == other.d

    def __ne__(self, other):
        return not (self == other)

    def __hash__(self):
        return hash(self.a) + hash(self.b) + hash(self.c) + hash(self.d)


if __name__ == "__main__":
    print(problem066())
