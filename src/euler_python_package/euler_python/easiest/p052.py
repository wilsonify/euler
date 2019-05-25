import itertools


def problem052():
    """


    It can be seen that the number, 125874, and its double, 251748, contain
       exactly the same digits, but in a different order.

       Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
       contain the same digits.
    """

    def cond(i):
        return all(sorted(str(i)) == sorted(str(j * i)) for j in range(2, 7))

    ans = next(i for i in itertools.count(1) if cond(i))
    return ans


if __name__ == "__main__":
    print(problem052())
