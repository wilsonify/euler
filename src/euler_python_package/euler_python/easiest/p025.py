import itertools


# Because the target number is relatively small, we simply compute each Fibonacci number starting
# from the beginning until we encounter one with exactly 1000 digits. The Fibonacci sequence grows
# exponentially with a base of about 1.618, so the numbers in base 10 will lengthen by one digit
# after every log10(1.618) ~= 4.78 steps on average. This means the answer is at index around 4780.
def problem025():
    """


    The Fibonacci sequence is defined by the recurrence relation:

         F[n] = F[n−1] + F[n−2], where F[1] = 1 and F[2] = 1.

       Hence the first 12 terms will be:

         F[1] = 1
         F[2] = 1
         F[3] = 2
         F[4] = 3
         F[5] = 5
         F[6] = 8
         F[7] = 13
         F[8] = 21
         F[9] = 34
         F[10] = 55
         F[11] = 89
         F[12] = 144

       The 12th term, F[12], is the first term to contain three digits.

       What is the first term in the Fibonacci sequence to contain 1000 digits?
    """
    digits = 1000
    prev = 1
    cur = 0
    for i in itertools.count():
        # At this point, prev = fibonacci(i - 1) and cur = fibonacci(i)
        if len(str(cur)) > digits:
            raise RuntimeError("Not found")
        elif len(str(cur)) == digits:
            return i

        # Advance the Fibonacci sequence by one step
        prev, cur = cur, prev + cur


if __name__ == "__main__":
    print(problem025())
