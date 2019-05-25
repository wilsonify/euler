
# 
# 
#
#
from euler_python.utils import eulerlib
import itertools


def problem142():
    # Finds any summation s = x+y+z such that s < limit, 0 < z < y < x, and these are
    # perfect squares: x+y, x-y, x+z, x-z, y+z, y-z. Returns -1 if none is found.
    # Suppose we let x + y = a^2 and x - y = b^2, so that they are always square.
    # Then x = (a^2 + b^2) / 2 and y = (a^2 - b^2) / 2. By ensuring a > b > 0, we have x > y > 0.
    # Now z < y and z < limit - x - y. Let y + z = c^2, then explicitly check
    # if x+z, x-z, and y-z are square.
    def find_sum(limit):
        for a in itertools.count(1):
            if a * a >= limit:
                break
            for b in reversed(range(1, a)):
                if (a + b) % 2 != 0:  # Need them to be both odd or both even so that we get integers for x and y
                    continue
                x = (a * a + b * b) // 2
                y = (a * a - b * b) // 2
                if x + y + 1 >= limit:  # Because z >= 1
                    continue

                zlimit = min(y, limit - x - y)
                for c in itertools.count(eulerlib.sqrt(y) + 1):
                    z = c * c - y
                    if z >= zlimit:
                        break
                    if issquare[x + z] and issquare[x - z] and issquare[y - z]:
                        return x + y + z
        return None

    sumlimit = 10
    # Raise the limit until a summation is found
    while True:
        issquare = [False] * sumlimit
        for i in range(eulerlib.sqrt(len(issquare) - 1) + 1):
            issquare[i * i] = True

        summation = find_sum(sumlimit)
        if summation is not None:
            break
        sumlimit *= 10

    # Lower the limit until now summation is found
    while True:
        summation = find_sum(sumlimit)
        if summation is None:  # No smaller summation found
            return (sumlimit)
        sumlimit = summation


if __name__ == "__main__":
    print(problem142())
