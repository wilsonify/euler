def problem091():
    """


    The points P (x[1], y[1]) and Q (x[2], y[2]) are plotted at integer
       co-ordinates and are joined to the origin, O(0,0), to form ΔOPQ.

       There are exactly fourteen triangles containing a right angle that can be
       formed when each co-ordinate lies between 0 and 2 inclusive; that is,
       0 ≤ x[1], y[1], x[2], y[2] ≤ 2.

       Given that 0 ≤ x[1], y[1], x[2], y[2] ≤ 50, how many right triangles can
       be formed?
    p_091_1.gif
       p_091_2.gif
    """

    LIMIT = 51
    ans = sum(
        1
        for x1 in range(LIMIT)
        for y1 in range(LIMIT)
        for x2 in range(LIMIT)
        for y2 in range(LIMIT)
        # For uniqueness, ensure that (x1,y1) has a larger angle than (x2,y2)
        if y2 * x1 < y1 * x2 and is_right_triangle(x1, y1, x2, y2)
    )
    return ans


# Tests whether the three points {(0,0), (x1,y1), (x2,y2)} form a right triangle.
def is_right_triangle(x1, y1, x2, y2):
    a = x1 ** 2 + y1 ** 2
    b = x2 ** 2 + y2 ** 2
    c = (x2 - x1) ** 2 + (y2 - y1) ** 2
    return (a + b == c) or (b + c == a) or (c + a == b)


if __name__ == "__main__":
    print(problem091())
