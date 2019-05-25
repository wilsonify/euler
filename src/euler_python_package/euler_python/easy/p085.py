from euler_python.utils import eulerlib


def problem085():
    """


    By counting carefully it can be seen that a rectangular grid measuring 3
       by 2 contains eighteen rectangles:

       Although there exists no rectangular grid that contains exactly two
       million rectangles, find the area of the grid with the nearest solution.
    p_085.gif
    """
    target = 2000000
    end = eulerlib.sqrt(target) + 1
    gen = ((w, h) for w in range(1, end) for h in range(1, end))

    def func(wh):
        return abs(num_rectangles(*wh) - target)

    ans = min(gen, key=func)
    return ans[0] * ans[1]


def num_rectangles(m, n):
    return (m + 1) * m * (n + 1) * n // 4  # A bit more than m^2 n^2 / 4


if __name__ == "__main__":
    print(problem085())
