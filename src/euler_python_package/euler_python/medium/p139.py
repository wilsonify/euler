

#
#
import math
from euler_python.utils import eulerlib


def problem139():
    LIMIT = 100000000

    # Pythagorean triples theorem:
    #   Every primitive Pythagorean triple with a odd and b even can be expressed as
    #   a = st, b = (s^2-t^2)/2, c = (s^2+t^2)/2, where s > t > 0 are coprime odd integers.
    ans = 0
    for s in range(3, eulerlib.sqrt(LIMIT * 2), 2):
        for t in range(1, s, 2):
            a = s * t
            b = (s * s - t * t) // 2
            c = (s * s + t * t) // 2
            p = a + b + c
            if p >= LIMIT:
                break
            if c % (a - b) == 0 and math.gcd(s, t) == 1:
                ans += (LIMIT - 1) // p
    return ans


if __name__ == "__main__":
    print(problem139())
