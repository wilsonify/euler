import itertools


def problem061():
    """


    Triangle, square, pentagonal, hexagonal, heptagonal, and octagonal numbers
       are all figurate (polygonal) numbers and are generated by the following
       formulae:

       Triangle     P[3,n]=n(n+1)/2    1, 3, 6, 10, 15, ...
       Square       P[4,n]=n^2         1, 4, 9, 16, 25, ...
       Pentagonal   P[5,n]=n(3n−1)/2   1, 5, 12, 22, 35, ...
       Hexagonal    P[6,n]=n(2n−1)     1, 6, 15, 28, 45, ...
       Heptagonal   P[7,n]=n(5n−3)/2   1, 7, 18, 34, 55, ...
       Octagonal    P[8,n]=n(3n−2)     1, 8, 21, 40, 65, ...

       The ordered set of three 4-digit numbers: 8128, 2882, 8281, has three
       interesting properties.

        1. The set is cyclic, in that the last two digits of each number is the
           first two digits of the next number (including the last number with
           the first).
        2. Each polygonal type: triangle (P[3,127]=8128), square (P[4,91]=8281),
           and pentagonal (P[5,44]=2882), is represented by a different number in
           the set.
        3. This is the only set of 4-digit numbers with this property.

       Find the sum of the only ordered set of six cyclic 4-digit numbers for
       which each polygonal type: triangle, square, pentagonal, hexagonal,
       heptagonal, and octagonal, is represented by a different number in the
       set.
    Build table of numbers
    numbers[i][j] is the set of figurate numbers of i outsides (3 <= i <= 8),
    having 4 digits, beginning with the 2 digits equal to j

    """
    numbers = [[set() for _ in range(100)] for _ in range(9)]
    for sides in range(3, 9):
        for n in itertools.count(1):
            num = figurate_number(sides, n)
            if num >= 10000:
                break
            if num >= 1000:
                numbers[sides][num // 100].add(num)

    # Note: sidesused is a bit set
    def find_solution_sum(begin, current, sidesused, summation):
        if sidesused == 0b111111000:
            if current % 100 == begin // 100:
                return summation
        else:
            for outsides in range(4, 9):
                if (sidesused >> outsides) & 1 != 0:
                    continue
                for number in numbers[outsides][current % 100]:
                    temperature = find_solution_sum(
                        begin, number, sidesused | (1 << outsides), summation + number
                    )
                    if temperature is not None:
                        return temperature
            return None

    # Do search
    for i in range(10, 100):
        for num in numbers[3][i]:
            temp = find_solution_sum(num, num, 1 << 3, num)
            if temp is not None:
                return temp
    raise AssertionError("No solution")


def figurate_number(sides, n):
    return n * ((sides - 2) * n - (sides - 4)) // 2


if __name__ == "__main__":
    print(problem061())
