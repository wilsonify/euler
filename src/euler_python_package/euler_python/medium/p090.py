from euler_python.utils import eulerlib


def problem090():
    """


    Each of the six faces on a cube has a different digit (0 to 9) written on
       it; the same is done to a second cube. By placing the two cubes
       side-by-side in different positions we can form a variety of 2-digit
       numbers.

       For example, the square number 64 could be formed:

       In fact, by carefully choosing the digits on both cubes it is possible to
       display all of the square numbers below one-hundred: 01, 04, 09, 16, 25,
       36, 49, 64, and 81.

       For example, one way this can be achieved is by placing {0, 5, 6, 7, 8, 9}
       on one cube and {1, 2, 3, 4, 8, 9} on the other cube.

       However, for this
    Problem we shall allow the 6 or 9 to be turned
       upside-down so that an arrangement like {0, 5, 6, 7, 8, 9} and {1, 2, 3,
       4, 6, 7} allows for all nine square numbers to be displayed; otherwise it
       would be impossible to obtain 09.

       In determining a distinct arrangement we are interested in the digits on
       each cube, not the order.

       {1, 2, 3, 4, 5, 6} is equivalent to {3, 6, 4, 1, 2, 5}
       {1, 2, 3, 4, 5, 6} is distinct from {1, 2, 3, 4, 5, 9}

       But because we are allowing 6 and 9 to be reversed, the two distinct sets
       in the last example both represent the extended set {1, 2, 3, 4, 5, 6, 9}
       for the purpose of forming 2-digit numbers.

       How many distinct arrangements of the two cubes allow for all of the
       square numbers to be displayed?
    p_090.gif
    """

    # Each die has (10 choose 6) arrangements, so we have at most 44100 arrangements to check
    ans = sum(
        1
        for i in range(1 << 10)
        for j in range(i, 1 << 10)  # Ensure i <= j to force the dice to be orderless
        # If both have Hamming weight of 6
        if eulerlib.popcount(i) == eulerlib.popcount(j) == 6
        and is_arrangement_valid(i, j)
    )
    return ans


def is_arrangement_valid(a, b):
    if test_bit(a, 6) or test_bit(a, 9):
        a |= (1 << 6) | (1 << 9)
    if test_bit(b, 6) or test_bit(b, 9):
        b |= (1 << 6) | (1 << 9)
    return all(
        ((test_bit(a, c) and test_bit(b, d)) or (test_bit(a, d) and test_bit(b, c)))
        for (c, d) in SQUARES
    )


def test_bit(x, i):
    return ((x >> i) & 1) != 0


SQUARES = [(i ** 2 // 10, i ** 2 % 10) for i in range(1, 10)]

if __name__ == "__main__":
    print(problem090())
