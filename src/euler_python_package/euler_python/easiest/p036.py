def problem036():
    """


    The decimal number, 585 = 1001001001[2] (binary), is palindromic in both
       bases.

       Find the sum of all numbers, less than one million, which are palindromic
       in base 10 and base 2.

       (Please note that the palindromic number, in either base, may not include
       leading zeros.)
    """

    ans = sum(i for i in range(1000000) if is_decimal_binary_palindrome(i))
    return ans


def is_decimal_binary_palindrome(n):
    s = str(n)
    if s != s[::-1]:
        return False
    t = bin(n)[2:]
    return t == t[::-1]


if __name__ == "__main__":
    print(problem036())
