from euler_python.utils import eulerlib


def problem035():
    """


    The number, 197, is called a circular prime because all rotations of the
       digits: 197, 971, and 719, are themselves prime.

       There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37,
       71, 73, 79, and 97.

       How many circular primes are there below one million?
    """

    isprime = eulerlib.list_primality(999999)

    def is_circular_prime(n):
        s = str(n)
        return all(isprime[int(s[i:] + s[: i])] for i in range(len(s)))

    ans = sum(1
              for i in range(len(isprime))
              if is_circular_prime(i))
    return ans


if __name__ == "__main__":
    print(problem035())
