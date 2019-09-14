import itertools

import math


def problem086():
    """


    A spider, S, sits in one corner of a cuboid room, measuring 6 by 5 by 3,
       and a fly, F, sits in the opposite corner. By travelling on the surfaces
       of the room the shortest "straight line" distance from S to F is 10 and
       the path is shown on the diagram.

       However, there are up to three "shortest" path candidates for any given
       cuboid and the shortest route doesn't always have integer length.

       By considering all cuboid rooms with integer dimensions, up to a maximum
       size of M by M by M, there are exactly 2060 cuboids for which the shortest
       route has integer length when M=100, and this is the least value of M for
       which the number of solutions first exceeds two thousand; the number of
       solutions is 1975 when M=99.

       Find the least value of M such that the number of solutions first exceeds
       one million.
    p_086.gif
    """

    # solutions[k] is the set of all solutions where the largest side has length k.
    # A solution is a triple (x, y, z) such that 0 < x <= y <= z, and in the rectangular prism with dimensions x * y * z,
    # the shortest surface path from one vertex to the opposite vertex has an integral length.
    solutions = []

    # Generates all solutions where the largest side has length less than 'limit'.
    def generate_solutions():
        # Pythagorean triples theorem:
        #   Every primitive Pythagorean triple with a odd and b even can be expressed as
        #   a = st, b = (s^2-t^2)/2, c = (s^2+t^2)/2, where s > t > 0 are coprime odd integers.
        # Now generate all Pythagorean triples, including non-primitive ones.
        for s in itertools.count(3, 2):
            for t in range(s - 2, 0, -2):
                if s * s // 2 >= limit * 3:
                    return

                if math.gcd(s, t) == 1:
                    for k in itertools.count(1):
                        a = s * t * k
                        b = (s * s - t * t) // 2 * k
                        c = (s * s + t * t) // 2 * k
                        if a >= limit and b >= limit:
                            break
                        find_splits(a, b, c)
                        find_splits(b, a, c)

    # Assumes that a^2 + b^2 = c^2.
    def find_splits(a, b, c):
        z = b
        for x in range(1, a):
            y = a - x
            if y < x:
                break
            if c * c == min(
                    (x + y) * (x + y) + z * z,
                    (y + z) * (y + z) + x * x,
                    (z + x) * (z + x) + y * y,
            ):
                temp = max(x, y, z)
                if temp < limit:
                    # Add canonical solution
                    item = tuple(sorted((x, y, z)))
                    solutions[temp].add(item)

    # cumulativesolutions[m] = len(solutions[0]) + len(solutions[1]) + ... + len(solutions[m]).
    cumulativesolutions = [0]

    limit = 1
    while True:
        # Extend the solutions list with blank sets
        while len(solutions) < limit:
            solutions.append(set())

        generate_solutions()

        # Compute the number of cumulative solutions up to and including a certain maximum size
        for i in range(len(cumulativesolutions), limit):
            sum = cumulativesolutions[i - 1] + len(solutions[i])
            cumulativesolutions.append(sum)
            if sum > 1000000:
                return i

        # Raise the limit and keep searching
        limit *= 2


if __name__ == "__main__":
    print(problem086())
