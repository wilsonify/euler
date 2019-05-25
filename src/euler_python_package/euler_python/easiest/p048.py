def problem048():
    """


    The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

       Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
    """

    modulo = 10 ** 10
    ans = sum(pow(i, i, modulo) for i in range(1, 1001)) % modulo
    return ans


if __name__ == "__main__":
    print(problem048())
