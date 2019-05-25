import fractions
import itertools

from euler_python.utils import eulerlib


def problem093():
    """


    By using each of the digits from the set, {1, 2, 3, 4}, exactly once, and
       making use of the four arithmetic operations (+, −, *, /) and
       brackets/parentheses, it is possible to form different positive integer
       targets.

       For example,

       8 = (4 * (1 + 3)) / 2
       14 = 4 * (3 + 1 / 2)
       19 = 4 * (2 + 3) − 1
       36 = 3 * 4 * (2 + 1)

       Note that concatenations of the digits, like 12 + 34, are not allowed.

       Using the set, {1, 2, 3, 4}, it is possible to obtain thirty-one different
       target numbers of which 36 is the maximum, and each of the numbers 1 to 28
       can be obtained before encountering the first non-expressible number.

       Find the set of four distinct digits, a < b < c < d, for which the longest
       set of consecutive positive integers, 1 to n, can be obtained, giving your
       answer as a string: abcd.
    """

    ans = max(((a, b, c, d)
               for a in range(1, 10)
               for b in range(a + 1, 10)
               for c in range(b + 1, 10)
               for d in range(c + 1, 10)),
              key=longest_consecutive)
    return int("".join(str(x) for x in ans))


def longest_consecutive(abcd):
    a, b, c, d = abcd
    expressible = set()

    # Try all possible orderings of operands and operators
    ops = [0, 0, 0, a, b, c, d]  # 0 = operator slot, 1 to 9 = literal operand
    while True:

        # Try all possibilities for the 3 operators
        for i in range(64):
            stack = []
            j = 0  # Operator index

            stackunderflow = False
            divbyzero = False
            for op in ops:
                if 1 <= op <= 9:  # Operand
                    stack.append(fractions.Fraction(op))
                elif op == 0:  # Operator
                    if len(stack) < 2:
                        stackunderflow = True
                        break
                    right = stack.pop()
                    left = stack.pop()
                    oper = (i >> (j * 2)) & 3
                    if oper == 0:
                        stack.append(left + right)
                    elif oper == 1:
                        stack.append(left - right)
                    elif oper == 2:
                        stack.append(left * right)
                    elif oper == 3:
                        if right.numerator == 0:
                            divbyzero = True
                            break
                        stack.append(left / right)
                    else:
                        raise AssertionError()
                    j += 1  # Consume an operator
                else:
                    raise AssertionError()

            if stackunderflow:
                break
            if divbyzero:
                continue
            if len(stack) != 1:
                raise AssertionError()

            result = stack.pop()
            if result.denominator == 1:
                expressible.add(result.numerator)

        if not eulerlib.next_permutation(ops):
            break

    # Find largest set of consecutive expressible integers starting from 1
    return next(i for i in itertools.count(1) if (i not in expressible)) - 1


if __name__ == "__main__":
    print(problem093())
