def sum_multiples_of_3_or_5_below_n(n):
    """

       If we list all the natural numbers below 10 that are multiples of 3 or 5,
       we get 3, 5, 6 and 9. The sum of these multiples is 23.



    """
    return sum(x for x in range(n) if (x % 3 == 0 or x % 5 == 0))


def problem001():
    """
    Find the sum of all the multiples of 3 or 5 below 1000.
    """
    ans = sum_multiples_of_3_or_5_below_n(1000)
    return ans


if __name__ == "__main__":
    print(problem001())
