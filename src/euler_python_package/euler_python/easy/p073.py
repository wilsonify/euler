def problem073():
    """
    Consider the fraction, n/d, where n and d are positive integers. If n<d
       and HCF(n,d)=1, it is called a reduced proper fraction.

       If we list the set of reduced proper fractions for d ≤ 8 in ascending
       order of size, we get:

       1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3,
                              5/7, 3/4, 4/5, 5/6, 6/7, 7/8

       It can be seen that there are 3 fractions between 1/3 and 1/2.

       How many fractions lie between 1/3 and 1/2 in the sorted set of reduced
       proper fractions for d ≤ 12,000?



    The Stern-Brocot tree is an infinite binary search tree of all positive rational numbers,
    where each number appears only once and is in lowest terms.
    It is formed by starting with the two sentinels 0/1 and 1/1. Iterating infinitely in any order,
    between any two currently adjacent fractions Ln/Ld and Rn/Rd, insert a new fraction (Ln+Rn)/(Ld+Rd).
    See MathWorld for a visualization: http://mathworld.wolfram.com/Stern-BrocotTree.html

    The natural algorithm is as follows:
      Counts the number of reduced fractions n/d such that leftN/leftD < n/d < rightN/rightD and d <= 12000.
      leftN/leftD and rightN/rightD must be adjacent in the Stern-Brocot tree at some point in the generation process.
      def stern_brocot_count(leftn, leftd, rightn, rightd):
        d = leftd + rightd
        if d > 12000:
          return 0
        else:
          n = leftn + rightn
          return 1 + stern_brocot_count(leftn, leftd, n, d) + stern_brocot_count(n, d, rightn, rightd)
    But instead we use depth-first search on an explicit stack, because having
    a large number of stack frames seems to be supported on Linux but not on Windows.

    """
    ans = 0
    stack = [(1, 3, 1, 2)]
    while len(stack) > 0:
        leftn, leftd, rightn, rightd = stack.pop()
        d = leftd + rightd
        if d <= 12000:
            n = leftn + rightn
            ans += 1
            stack.append((n, d, rightn, rightd))
            stack.append((leftn, leftd, n, d))
    return ans


if __name__ == "__main__":
    print(problem073())
