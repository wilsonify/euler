from euler_python.utils import eulerlib


def problem387():
    """
       A Harshad or Niven number is a number that is divisible by the sum of its
       digits.
       201 is a Harshad number because it is divisible by 3 (the sum of its
       digits.)
       When we truncate the last digit from 201, we get 20, which is a Harshad
       number.
       When we truncate the last digit from 20, we get 2, which is also a Harshad
       number.
       Let's call a Harshad number that, while recursively truncating the last
       digit, always results in a Harshad number a right truncatable Harshad
       number.

       Also:
       201/3=67 which is prime.
       Let's call a Harshad number that, when divided by the sum of its digits,
       results in a prime a strong Harshad number.

       Now take the number 2011 which is prime.
       When we truncate the last digit from it we get 201, a strong Harshad
       number that is also right truncatable.
       Let's call such primes strong, right truncatable Harshad primes.

       You are given that the sum of the strong, right truncatable Harshad primes
       less than 10000 is 90619.

       Find the sum of the strong, right truncatable Harshad primes less than
       10^14.
    """
    limit = 10 ** 14

    # Use a list container as a hack, because Python 2 does not support 'nonlocal' variables
    ans = [0]

    # Note: n must be a right-truncatable Harshad number, and the other arguments are properties of the number n.
    def find_harshad_primes(n, digitsum, isstrong):
        # Shift left by 1 digit, and try all 10 possibilities for the rightmost digit
        m = n * 10
        s = digitsum
        for iteration in range(10):
            if m >= limit:
                break
            if isstrong and eulerlib.is_prime(m):
                ans[0] += m
            if m % s == 0:
                find_harshad_primes(m, s, eulerlib.is_prime(m // s))
            m += 1
            s += 1

    for i in range(1, 10):  # All one-digit numbers are trivially Harshad numbers
        find_harshad_primes(i, i, False)
    return ans[0]


if __name__ == "__main__":
    print(problem387())
