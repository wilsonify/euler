import itertools


def problem062():
    """


    The cube, 41063625 (345^3), can be permuted to produce two other cubes:
       56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest
       cube which has exactly three permutations of its digits which are also
       cube.

       Find the smallest cube for which exactly five permutations of its digits
       are cube.
    """
    numdigits = 0
    data = {}  # str numclass -> (int lowest, int count)
    for i in itertools.count():
        digits = [int(c) for c in str(i ** 3)]
        digits.sort()
        numclass = "".join(str(d) for d in digits)

        if len(numclass) > numdigits:
            # Process and flush data for smaller number of digits
            candidates = [lowest for (lowest, count) in data.values() if count == 5]
            if len(candidates) > 0:
                return min(candidates) ** 3
            data = {}
            numdigits = len(numclass)

        lowest, count = data.get(numclass, (i, 0))
        data[numclass] = (lowest, count + 1)


if __name__ == "__main__":
    print(problem062())
