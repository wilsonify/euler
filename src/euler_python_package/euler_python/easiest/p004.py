def largest_palindrome_from_product_of_two_n_digit_numbers(n):
    """
    A palindromic number reads the same both ways. The largest palindrome made
    from the product of two 2-digit numbers is 9009 = 91 × 99.

    :param n:
    :return:
    """
    ans = max(i * j
              for i in range(10 ** (n - 1), 10 ** n)
              for j in range(10 ** (n - 1), 10 ** n)
              if str(i * j) == str(i * j)[:: -1])
    return ans


def problem004():
    """
    Find the largest palindrome made from the product of two 3-digit numbers.
    """
    return largest_palindrome_from_product_of_two_n_digit_numbers(3)


if __name__ == "__main__":
    print(problem004())
