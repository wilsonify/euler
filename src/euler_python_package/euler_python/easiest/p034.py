"""


145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

   Find the sum of all numbers which are equal to the sum of the factorial of
   their digits.

   Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

import math


def factorial_digit_sum(input_n):
    """

    :param input_n:
    :return:
    """
    result = 0
    while input_n >= 10000:
        result += FACTORIAL_DIGITS_SUM_WITH_LEADING_ZEROS[input_n % 10000]
        input_n //= 10000
    return result + FACTORIAL_DIGITS_SUM_WITHOUT_LEADING_ZEROS[input_n]


FACTORIAL_DIGITS_SUM_WITHOUT_LEADING_ZEROS = [sum(math.factorial(int(c)) for c in str(i)) for i in range(10000)]
FACTORIAL_DIGITS_SUM_WITH_LEADING_ZEROS = [sum(math.factorial(int(c)) for c in str(i).zfill(4)) for i in range(10000)]


def sum_factorial_digits(upper_bound=10000000):
    """

    145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

       Find the sum of all numbers which are equal to the sum of the factorial of
       their digits.

       Note: as 1! = 1 and 2! = 2 are not sums they are not included.
    """

    ans = sum(i for i in range(3, upper_bound) if i == factorial_digit_sum(i))
    return ans


def problem034():
    """

    # As stated in the problem, 1 = 1! and 2 = 2! are excluded.
    # If a number has at least n >= 8 digits, then even if every digit is 9,
    # n * 9! is still less than the number (which is at least 10^n).


    :return:
    """
    return sum_factorial_digits(upper_bound=10000000)


if __name__ == "__main__":
    print(problem034())
