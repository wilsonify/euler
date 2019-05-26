"""


Surprisingly there are only three numbers that can be written as the sum
   of fourth powers of their digits:

     1634 = 1^4 + 6^4 + 3^4 + 4^4
     8208 = 8^4 + 2^4 + 0^4 + 8^4
     9474 = 9^4 + 4^4 + 7^4 + 4^4

   As 1 = 1^4 is not a sum it is not included.

   The sum of these numbers is 1634 + 8208 + 9474 = 19316.

   Find the sum of all the numbers that can be written as the sum of fifth
   powers of their digits.
"""


def fifth_power_digit_sum(input_n):
    """
        Surprisingly there are only three numbers that can be written as the sum
       of fourth powers of their digits:

         1634 = 1^4 + 6^4 + 3^4 + 4^4
         8208 = 8^4 + 2^4 + 0^4 + 8^4
         9474 = 9^4 + 4^4 + 7^4 + 4^4

       As 1 = 1^4 is not a sum it is not included.

       The sum of these numbers is 1634 + 8208 + 9474 = 19316.


    :param input_n:
    :return:
    """
    return sum(int(c) ** 5 for c in str(input_n))


def sum_fifth_power_digits(upper_bound=10 ** 6):
    """
       Find the sum of all the numbers that can be written as the sum of fifth
       powers of their digits.
    """

    ans = sum(i for i in range(2, upper_bound) if i == fifth_power_digit_sum(i))
    return ans


def problem030():
    """
    As stated in the problem, 1 = 1^5 is excluded.
    If a number has at least n >= 7 digits, then even if every digit is 9,
    n * 9^5 is still less than the number (which is at least 10^n).

    :return:
    """
    return sum_fifth_power_digits(upper_bound=10 ** 6)


if __name__ == "__main__":
    print(problem030())
