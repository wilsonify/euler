#
#
from euler_python.utils import eulerlib


def problem050():
    """


    The prime 41, can be written as the summation of six consecutive primes:

                              41 = 2 + 3 + 5 + 7 + 11 + 13

       This is the longest summation of consecutive primes that adds to a prime below
       one-hundred.

       The longest summation of consecutive primes below one-thousand that adds to a
       prime, contains 21 terms, and is equal to 953.

       Which prime, below one-million, can be written as the summation of the most
       consecutive primes?
    """
    ans = 0
    isprime = eulerlib.list_primality(999999)
    primes = eulerlib.list_primes(999999)
    consecutive = 0
    for i in range(len(primes)):
        summation = primes[i]
        consec = 1
        for j in range(i + 1, len(primes)):
            summation += primes[j]
            consec += 1
            if summation >= len(isprime):
                break
            if isprime[summation] and consec > consecutive:
                ans = summation
                consecutive = consec
    return ans


if __name__ == "__main__":
    print(problem050())
