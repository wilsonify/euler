"""
   The number, 197, is called a circular prime because all rotations of the
   digits: 197, 971, and 719, are themselves prime.

   There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37,
   71, 73, 79, and 97.

   How many circular primes are there below one million?
"""
from euler_python.utils import eulerlib


def count_circular_primes(upper_bound=999999):
    """
       The number, 197, is called a circular prime because all rotations of the
       digits: 197, 971, and 719, are themselves prime.

       There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37,
       71, 73, 79, and 97.

       How many circular primes are there below one million?
    """

    is_prime = eulerlib.list_primality(upper_bound)

    def is_circular_prime(input_n):
        n_string = str(input_n)
        return all(is_prime[int(n_string[i:] + n_string[: i])] for i in range(len(n_string)))

    ans = sum(1
              for i in range(len(is_prime))
              if is_circular_prime(i))
    return ans


def problem035():
    """
    :return:
    """
    return count_circular_primes(upper_bound=999999)


if __name__ == "__main__":
    print(problem035())
