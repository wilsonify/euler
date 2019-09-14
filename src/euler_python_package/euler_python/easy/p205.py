def problem205():
    """


    Peter has nine four-sided (pyramidal) dice, each with faces numbered 1, 2,
       3, 4.
       Colin has six six-sided (cubic) dice, each with faces numbered 1, 2, 3, 4,
       5, 6.

       Peter and Colin roll their dice and compare totals: the highest total
       wins. The result is a draw if the totals are equal.

       What is the probability that Pyramidal Pete beats Cubic Colin? Give your
       answer rounded to seven decimal places in the form 0.abcdefg
    """

    nine_pyramidal_pdf = [1]
    pyramidal_die_pdf = [0, 1, 1, 1, 1]
    for i in range(9):
        nine_pyramidal_pdf = convolve(nine_pyramidal_pdf, pyramidal_die_pdf)

    six_cubic_pdf = [1]
    cubic_die_pdf = [0, 1, 1, 1, 1, 1, 1]
    for i in range(6):
        six_cubic_pdf = convolve(six_cubic_pdf, cubic_die_pdf)

    ans = 0
    for i in range(len(nine_pyramidal_pdf)):
        ans += nine_pyramidal_pdf[i] * sum(six_cubic_pdf[:i])
    ans = float(ans) / (sum(nine_pyramidal_pdf) * sum(six_cubic_pdf))
    return float("{:.7f}".format(ans))


def convolve(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i in range(len(a)):
        for j in range(len(b)):
            c[i + j] += a[i] * b[j]
    return c


if __name__ == "__main__":
    print(problem205())
