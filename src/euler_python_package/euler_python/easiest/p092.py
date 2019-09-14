def problem092():
    """


    A number chain is created by continuously adding the square of the digits
       in a number to form a new number until it has been seen before.

       For example,

       44 → 32 → 13 → 10 → 1 → 1
       85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

       Therefore any chain that arrives at 1 or 89 will become stuck in an
       endless loop. What is most amazing is that EVERY starting number will
       eventually arrive at 1 or 89.

       How many starting numbers below ten million will arrive at 89?
    """
    ans = sum(1 for i in range(1, 10000000) if get_terminal(i) == 89)
    return ans


TERMINALS = (1, 89)


def get_terminal(n):
    while n not in TERMINALS:
        n = square_digit_sum(n)
    return n


def square_digit_sum(n):
    result = 0
    while n > 0:
        result += SQUARE_DIGITS_SUM[n % 1000]
        n //= 1000
    return result


SQUARE_DIGITS_SUM = [sum(int(c) ** 2 for c in str(i)) for i in range(1000)]

if __name__ == "__main__":
    print(problem092())
