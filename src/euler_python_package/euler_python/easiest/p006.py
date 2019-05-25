def problem006():
    """
    s  = N(N + 1) / 2.
    s2 = N(N + 1)(2N + 1) / 6.
    Hence s^2 - s2 = (N^4 / 4) + (N^3 / 6) - (N^2 / 4) - (N / 6).

    The sum of the squares of the first ten natural numbers is,

                          1^2 + 2^2 + ... + 10^2 = 385

   The square of the sum of the first ten natural numbers is,

                       (1 + 2 + ... + 10)^2 = 55^2 = 3025

   Hence the difference between the sum of the squares of the first ten
   natural numbers and the square of the sum is 3025 − 385 = 2640.

   Find the difference between the sum of the squares of the first one
   hundred natural numbers and the square of the sum.
   """

    number = 100
    s = sum(i for i in range(1, number + 1))
    s2 = sum(i ** 2 for i in range(1, number + 1))
    return s ** 2 - s2


if __name__ == "__main__":
    print(problem006())
