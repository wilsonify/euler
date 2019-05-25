def problem040():
    """


    An irrational decimal fraction is created by concatenating the positive
       integers:

                         0.123456789101112131415161718192021...

       It can be seen that the 12^th digit of the fractional part is 1.

       If d[n] represents the n^th digit of the fractional part, find the value
       of the following expression.

          d[1] × d[10] × d[100] × d[1000] × d[10000] × d[100000] × d[1000000]
    """

    s = "".join(str(i) for i in range(1, 1000000))
    ans = 1
    for i in range(7):
        ans *= int(s[10 ** i - 1])
    return ans


if __name__ == "__main__":
    print(problem040())
