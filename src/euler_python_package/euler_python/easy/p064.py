#
#
#
#
import math

from euler_python.utils import eulerlib


def problem064():
    """


    All square roots are periodic when written as continued fractions and can
       be written in the form:

       √N = a[0] +            1
                   a[1] +         1
                          a[2] +     1
                                 a[3] + ...

       For example, let us consider √23:

       √23 = 4 + √23 — 4 = 4 +    1    = 4 +       1
                                  1           1 +  √23 – 3
                                √23—4                 7

       If we continue we would get the following expansion:

       √23 = 4 +          1
                 1 +        1
                     3 +      1
                         1 +    1
                             8 + ...

       The process can be summarised as follows:

       a[0] = 4,     1    =   √23+4    = 1 +  √23—3
                   √23—4        7               7
       a[1] = 1,     7    =  7(√23+3)  = 3 +  √23—3
                   √23—3        14              2
       a[2] = 3,     2    =  2(√23+3)  = 1 +  √23—4
                   √23—3        14              7
       a[3] = 1,     7    =  7(√23+4)  = 8 +  √23—4
                   √23—4        7
       a[4] = 8,     1    =   √23+4    = 1 +  √23—3
                   √23—4        7               7
       a[5] = 1,     7    =  7(√23+3)  = 3 +  √23—3
                   √23—3        14              2
       a[6] = 3,     2    =  2(√23+3)  = 1 +  √23—4
                   √23—3        14              7
       a[7] = 1,     7    =  7(√23+4)  = 8 +  √23—4
                   √23—4        7

       It can be seen that the sequence is repeating. For conciseness, we use the
       notation √23 = [4;(1,3,1,8)], to indicate that the block (1,3,1,8) repeats
       indefinitely.

       The first ten continued fraction representations of (irrational) square
       roots are:

       √2=[1;(2)], period=1
       √3=[1;(1,2)], period=2
       √5=[2;(4)], period=1
       √6=[2;(2,4)], period=2
       √7=[2;(1,1,1,4)], period=4
       √8=[2;(1,4)], period=2
       √10=[3;(6)], period=1
       √11=[3;(3,6)], period=2
       √12= [3;(2,6)], period=2
       √13=[3;(1,1,1,1,6)], period=5

       Exactly four continued fractions, for N ≤ 13, have an odd period.

       How many continued fractions for N ≤ 10000 have an odd period?
    """
    ans = sum(
        1
        for i in range(1, 10001)
        if (
                not eulerlib.is_square(i) and get_sqrt_continued_fraction_period(i) % 2 == 1
        )
    )
    return ans


# Returns the period of the continued fraction of sqrt(n)
def get_sqrt_continued_fraction_period(n):
    seen = {}
    val = QuadraticSurd(0, 1, 1, n)
    while True:
        seen[val] = len(seen)
        val = (val - QuadraticSurd(val.floor(), 0, 1, val.d)).reciprocal()
        if val in seen:
            return len(seen) - seen[val]


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
            self.d,
        )

    def reciprocal(self):
        return QuadraticSurd(
            -self.a * self.c,
            self.b * self.c,
            self.b * self.b * self.d - self.a * self.a,
            self.d,
        )

    def floor(self):
        temp = eulerlib.sqrt(self.b * self.b * self.d)
        if self.b < 0:
            temp = -(temp + 1)
        temp += self.a
        if temp < 0:
            temp -= self.c - 1
        return temp // self.c

    def __eq__(self, other):
        return (
                self.a == other.a
                and self.b == other.b
                and self.c == other.c
                and self.d == other.d
        )

    def __ne__(self, other):
        return not (self == other)

    def __hash__(self):
        return hash(self.a) + hash(self.b) + hash(self.c) + hash(self.d)


if __name__ == "__main__":
    print(problem064())
