import itertools


def problem104():
    """


    The Fibonacci sequence is defined by the recurrence relation:

         F[n] = F[n−1] + F[n−2], where F[1] = 1 and F[2] = 1.

       It turns out that F[541], which contains 113 digits, is the first
       Fibonacci number for which the last nine digits are 1-9 pandigital
       (contain all the digits 1 to 9, but not necessarily in order). And
       F[2749], which contains 575 digits, is the first Fibonacci number for
       which the first nine digits are 1-9 pandigital.

       Given that F[k] is the first Fibonacci number for which the first nine
       digits AND the last nine digits are 1-9 pandigital, find k.
    """

    MOD = 10 ** 9
    a = 0
    b = 1
    i = 0
    for i in itertools.count():
        # Loop invariants: a == fib(i) % MOD, b == fib(i+1) % MOD
        if "".join(sorted(str(a))) == "123456789":  # If suffix is pandigital
            f = fibonacci(i)[0]
            if "".join(sorted(str(f)[:9])) == "123456789":  # If prefix is pandigital
                return i
        a, b = b, (a + b) % MOD
    return i


# Returns the tuple (F(n), F(n+1)), computed by the fast doubling method.
def fibonacci(n):
    if n == 0:
        return (0, 1)
    else:
        a, b = fibonacci(n // 2)
        c = a * (b * 2 - a)
        d = a * a + b * b
        if n % 2 == 0:
            return (c, d)
        else:
            return (d, c + d)


if __name__ == "__main__":
    print(problem104())
