from euler_python.utils import eulerlib


# Suppose the box has b blue discs and r red discs.
# The probability of taking 2 blue discs is [b / (b + r)] * [(b - 1) / (b + r - 1)],
# which we want to be equal to 1/2. Rearrange the equation:
#   [b(b - 1)] / [(b + r)(b + r - 1)] = 1 / 2.
#   2b(b - 1) = (b + r)(b + r - 1).
#   2b^2 - 2b = b^2 + br - b + br + r^2 - r.
#   b^2 - b = r^2 + 2br - r.
#   b^2 - (2r + 1)b + (r - r^2) = 0.
# Apply the quadratic equation to solve for b:
#   b = [(2r + 1) +/- sqrt((2r + 1)^2 - 4(r - r^2))] / 2
#     = r + [1 +/- sqrt(8r^2 + 1)]/2
#     = r + [sqrt(8r^2 + 1) + 1]/2.  (Discard the minus solution because it would make b < r)
#
# For b to be an integer, we need sqrt(8r^2 + 1) to be odd, and also 8r^2 + 1 be a perfect square.
# Assume 8y^2 + 1 = x^2 for some integer x > 0.
# We can see this is in fact a Pell's equation: x^2 - 8y^2 = 1.
#
# Suppose we have the solution (x0, y0) such that x0 > 0 and x0 is as small as possible.
# This is called the fundamental solution, and all other solutions be derived from it (proven elsewhere).
# Suppose (x0, y0) and (x1, y1) are solutions. Then we have:
#   x0^2 - 8*y0^2 = 1.
#   (x0 + y0*sqrt(8))(x0 - y0*sqrt(8)) = 1.
#   (x1 + y1*sqrt(8))(x1 - y1*sqrt(8)) = 1.  (Similarly)
# Multiply them together:
#   [(x0 + y0*sqrt(8))(x0 - y0*sqrt(8))][(x1 + y1*sqrt(8))(x1 - y1*sqrt(8))] = 1 * 1.
#   [(x0 + y0*sqrt(8))(x1 + y1*sqrt(8))][(x0 - y0*sqrt(8))(x1 - y1*sqrt(8))] = 1.
#   [x0*x1 + x0*y1*sqrt(8) + x1*y0*sqrt(8) + 8y0*y1][x0*x1 - x0*y1*sqrt(8) - x1*y0*sqrt(8) + 8y0*y1] = 1.
#   [(x0*x1 + 8y0*y1) + (x0*y1 + x1*y0)*sqrt(8)][(x0*x1 + 8y0*y1) - (x0*y1 + x1*y0)*sqrt(8)] = 1.
#   (x0*x1 + 8y0*y1)^2 - 8*(x0*y1 + x1*y0)^2 = 1.
# Therefore (x0*x1 + 8y0*y1, x0*y1 + x1*y0) is also a solution.
# By inspection, the fundamental solution is (3, 1).
def problem100():
    """


    If a box contains twenty-one coloured discs, composed of fifteen blue
       discs and six red discs, and two discs were taken at random, it can be
       seen that the probability of taking two blue discs, P(BB) =
       (15/21)×(14/20) = 1/2.

       The next such arrangement, for which there is exactly 50% chance of taking
       two blue discs at random, is a box containing eighty-five blue discs and
       thirty-five red discs.

       By finding the first arrangement to contain over 10^12 = 1,000,000,000,000
       discs in total, determine the number of blue discs that the box would
       contain.
    """

    # Fundamental solution
    x0 = 3
    y0 = 1

    # Current solution
    x = x0
    y = y0  # An alias for the number of red discs
    while True:
        # Check if this solution is acceptable
        sqrt = eulerlib.sqrt(y ** 2 * 8 + 1)
        if sqrt % 2 == 1:  # Is odd
            blue = (sqrt + 1) // 2 + y
            if blue + y > 10 ** 12:
                return blue

        # Create the next bigger solution
        nextx = x * x0 + y * y0 * 8
        nexty = x * y0 + y * x0
        x = nextx
        y = nexty


if __name__ == "__main__":
    print(problem100())
