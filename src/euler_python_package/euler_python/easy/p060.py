from euler_python.utils import eulerlib


def problem060():
    """
    The primes 3, 7, 109, and 673, are quite remarkable. By taking any two
    primes and concatenating them in any order the result will always be
    prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The
    sum of these four primes, 792, represents the lowest sum for a set of four
    primes with this property.
    Find the lowest sum for a set of five primes for which any two primes
    concatenate to produce another prime.
    """

    prime_limit = 100000  # Arbitrary initial cutoff
    primes = eulerlib.list_primes(prime_limit)

    # Tries to find any suitable set and return its sum, or None if none is found.
    # A set is suitable if it contains only primes, its size is targetsize,
    # its sum is less than or equal to sumlimit, and each pair concatenates to a prime.
    # 'prefix' is an array of ascending indices into the 'primes' array,
    # which describes the set found so far.
    # The function blindly assumes that each pair of primes in 'prefix' concatenates to a prime.
    # For example, find_set_sum([1, 3, 28], 5, 10000) means "find the sum of any set
    # where the set has size 5, consists of primes with the lowest elements being [3, 7, 109],
    # has sum 10000 or less, and has each pair concatenating to form a prime".
    def find_set_sum(prefix, targetsize, sum_limitation):
        if len(prefix) == targetsize:
            return sum(primes[i] for i in prefix)
        else:
            istart = 0 if (len(prefix) == 0) else (prefix[-1] + 1)
            for i in range(istart, len(primes)):
                if primes[i] > sum_limitation:
                    break
                if all(
                        (is_concat_prime(i, j) and is_concat_prime(j, i)) for j in prefix
                ):
                    prefix.append(i)
                    result = find_set_sum(
                        prefix, targetsize, sum_limitation - primes[i]
                    )
                    prefix.pop()
                    if result is not None:
                        return result
            return None

    # Tests whether concat(primes[x], primes[y]) is a prime number, with memoization.
    @eulerlib.Memoize
    def is_concat_prime(x, y):
        return is_prime(int(str(primes[x]) + str(primes[y])))

    # Tests whether the given integer is prime. The implementation performs trial division,
    # first using the list of primes named 'primes', then switching to simple incrementation.
    # This requires the last number in 'primes' (if any) to be an odd number.
    def is_prime(x):
        if x < 0:
            raise ValueError()
        elif x in (0, 1):
            return False
        else:
            end = eulerlib.sqrt(x)
            for p in primes:
                if p > end:
                    break
                if x % p == 0:
                    return False
            for i in range(primes[-1] + 2, end + 1, 2):
                if x % i == 0:
                    return False
            return True

    sumlimit = prime_limit
    while True:
        setsum = find_set_sum([], 5, sumlimit - 1)
        if setsum is None:  # No smaller sum found
            return sumlimit
        sumlimit = setsum


if __name__ == "__main__":
    print(problem060())
