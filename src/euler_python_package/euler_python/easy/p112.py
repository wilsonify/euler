import itertools


def problem112():
    """


    Working from left-to-right if no digit is exceeded by the digit to its
       left it is called an increasing number; for example, 134468.

       Similarly if no digit is exceeded by the digit to its right it is called a
       decreasing number; for example, 66420.

       We shall call a positive integer that is neither increasing nor decreasing
       a "bouncy" number; for example, 155349.

       Clearly there cannot be any bouncy numbers below one-hundred, but just
       over half of the numbers below one-thousand (525) are bouncy. In fact, the
       least number for which the proportion of bouncy numbers first reaches 50%
       is 538.

       Surprisingly, bouncy numbers become more and more common and by the time
       we reach 21780 the proportion of bouncy numbers is equal to 90%.

       Find the least number for which the proportion of bouncy numbers is
       exactly 99%.
    """

    count = 0
    for i in itertools.count(1):
        s = str(i)
        t = "".join(sorted(s))
        if s != t and s[::-1] != t:
            count += 1  # i is bouncy
        if count * 100 == 99 * i:
            return i


if __name__ == "__main__":
    print(problem112())
