
from euler_python.utils import eulerlib
import array, itertools


# Let n be an arbitrary integer such that n >= 3.
# When we say that the modular inverse of m modulo n equals m itself,
# the formula is m^-1 = m mod n, which is equivalent to m^2 = 1 mod n.
# 
# We know that if n is prime, then m^2 = 1 mod n has exactly two solutions:
# m = 1, n-1. It is easy to verify that these two numbers are solutions.
# The equation factorizes as (m - 1)(m + 1) = 0 mod n. Because n is prime,
# the numbers form a field, and there are no zero divisors (two arbitrary
# non-zero numbers x and y such that xy = 0). Hence 1 and -1 mod n are
# the only possible solutions to the equation. (Note that for the excluded
# special prime case where n = 2, the solutions 1 and -1 are the same number.)
# 
# Suppose we can find the smallest prime factor of n quickly. (Note that if n is
# prime, then the smallest prime factor is n itself.) This can be achieved by
# building a table ahead of time, using a modification of the sieve of Eratosthenes.
# 
# Suppose that for every n' < n, we know the set of solutions to m^2 = 1 mod n'.
# This means whenever we solve the equation for the number n, we save its solutions
# in an ever-growing list, so that when we work on the next value of n we can access
# all possible smaller solutions. This is essentially an argument by strong induction.
# 
# Let p be the smallest prime factor of n. If p = n, then the set of
# solutions is {1, n - 1}, and we are finished with this value of n.
# 
# Otherwise p < n, and obviously n is an integer multiple of p. Because we are looking
# for values of m such that m^2 = 1 mod n, these candidate m values also must satisfy
# m^2 = 1 mod k for any k that divides n (i.e. k is a factor of n). We look at the set
# of solutions for the modulus k = n/p, which has already been solved because k < n.
# We know that any solution modulo n must be congruent to these solutions modulo k.
# Hence we can try to extend and check these old solutions by brute force. Namely, suppose
# m' is a solution modulo k. Then we check the sequence m = m' + 0k, m' + 1k, m' + 2k, ...,
# m' + (p-1)k modulo n. Because p is usually a small number, this isn't a lot of work to do.
def problem451():
    """


    Consider the number 15.
       There are eight positive numbers less than 15 which are coprime to 15: 1,
       2, 4, 7, 8, 11, 13, 14.
       The modular inverses of these numbers modulo 15 are: 1, 8, 4, 13, 2, 11,
       7, 14
       because
       1*1 mod 15=1
       2*8=16 mod 15=1
       4*4=16 mod 15=1
       7*13=91 mod 15=1
       11*11=121 mod 15=1
       14*14=196 mod 15=1

       Let I(n) be the largest positive number m smaller than n-1 such that the
       modular inverse of m modulo n equals m itself.
       So I(15)=11.
       Also I(100)=51 and I(7)=1.

       Find ∑I(n) for 3≤n≤2·10^7
    """

    LIMIT = 20000000

    # Build table of smallest prime factors
    smallestprimefactor = array.array("L", itertools.repeat(0, LIMIT + 1))
    end = eulerlib.sqrt(len(smallestprimefactor) - 1)
    for i in range(2, len(smallestprimefactor)):
        if smallestprimefactor[i] == 0:
            smallestprimefactor[i] = i
            if i <= end:
                for j in range(i * i, len(smallestprimefactor), i):
                    if smallestprimefactor[j] == 0:
                        smallestprimefactor[j] = i

    # Returns all the solutions (in ascending order) such that
    # for each k, 1 <= k < n and k^2 = 1 mod n.
    def get_solutions(n):
        if smallestprimefactor[n] == n:  # n is prime
            return (1, n - 1)
        else:
            temp = []
            p = smallestprimefactor[n]
            sols = solutions[n // p]
            for i in range(0, n, n // p):
                for j in sols:
                    k = i + j
                    if k * k % n == 1:
                        temp.append(k)
            return tuple(temp)

    # Process every integer in range
    solutions = [(), (), (1,)]
    ans = 0
    for i in range(3, LIMIT + 1):
        sols = get_solutions(i)
        if i <= LIMIT // 2:
            solutions.append(sols)
        ans += sols[-2]  # Second-largest solution
    return ans


if __name__ == "__main__":
    print(problem451())
