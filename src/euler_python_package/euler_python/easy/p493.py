"""
problem 493
"""
import fractions

import math

from euler_python.utils import eulerlib


def problem493():
    """
    :return:
    """
    num_colors = 7
    balls_per_color = 10
    num_picked = 20
    decimals = 9

    numerator = [0]

    def explore(remain, limit, history):
        if remain == 0:
            hist = list(history)
            while len(hist) < num_colors:
                hist.append(0)

            histogram = [0] * (balls_per_color + 1)
            for _ in hist:
                histogram[_] += 1

            count = math.factorial(num_colors)
            for _ in histogram:
                count = divide_exactly(count, math.factorial(_))

            for _ in hist:
                count *= eulerlib.binomial(balls_per_color, _)

            distinctcolors = len(history)
            numerator[0] += count * distinctcolors

        elif len(history) < num_colors:
            for i in range(min(limit, remain), 0, -1):
                history.append(i)
                explore(remain - i, i, history)
                history.pop()

    explore(num_picked, balls_per_color, [])
    denominator = eulerlib.binomial(num_colors * balls_per_color, num_picked)
    ans = fractions.Fraction(numerator[0], denominator)
    return float(format_fraction(ans, decimals))


def format_fraction(val, digits):
    """
    format_fraction
    :param val:
    :param digits:
    :return:
    """
    if digits <= 0:
        raise ValueError()
    if val < 0:
        return "-" + format_fraction(-val, digits)
    scaler = 10 ** digits
    val *= scaler
    flr = val.numerator // val.denominator
    rem = val % 1
    half = fractions.Fraction(1, 2)
    if rem > half or (rem == half and flr % 2 == 1):
        flr += 1
    return "{}.{}".format(flr // scaler, str(flr % scaler).zfill(digits))


def divide_exactly(input_x, input_y):
    """
    divide_exactly
    :param input_x:
    :param input_y:
    :return:
    """
    if input_x % input_y != 0:
        raise ValueError("Not divisible")
    return input_x // input_y


if __name__ == "__main__":
    print(problem493())
