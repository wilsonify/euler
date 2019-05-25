from euler_python.utils import eulerlib


def problem010():
    """
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
    Find the sum of all the primes below two million.

    Call the sieve of Eratosthenes and sum the primes found.
    """

    ans = sum(eulerlib.list_primes(1999999))
    return ans


if __name__ == "__main__":
    print(problem010())
