

# 
#
from euler_python.utils import eulerlib


def problem347():
    """


    The largest integer ≤ 100 that is only divisible by both the primes 2 and
       3 is 96, as 96=32*3=2^5*3.For two distinct primes p and q let M(p,q,N) be
       the largest positive integer ≤N only divisibleby both p and q and
       M(p,q,N)=0 if such a positive integer does not exist.

       E.g. M(2,3,100)=96.
       M(3,5,100)=75 and not 90 because 90 is divisible by 2 ,3 and 5.
       Also M(2,73,100)=0 because there does not exist a positive integer ≤ 100
       that is divisible by both 2 and 73.

       Let S(N) be the sum of all distinct M(p,q,N).S(100)=2262.

       Find S(10 000 000).
    """
    limit = 10000000

    possible = set()
    primes = eulerlib.list_primes(limit // 2)
    end = eulerlib.sqrt(limit)
    for i in range(len(primes)):
        p = primes[i]
        if p > end:
            break
        for j in range(i + 1, len(primes)):
            q = primes[j]
            lcm = p * q
            if lcm > limit:
                break
            multlimit = limit // lcm

            multiplier = 1
            while multiplier * p <= multlimit:
                multiplier *= p
            maxmult = multiplier
            while multiplier % p == 0:
                multiplier //= p
                while multiplier * q <= multlimit:
                    multiplier *= q
                maxmult = max(multiplier, maxmult)
            possible.add(maxmult * lcm)

    ans = sum(possible)
    return ans


if __name__ == "__main__":
    print(problem347())
