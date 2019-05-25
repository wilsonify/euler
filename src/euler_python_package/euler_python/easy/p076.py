def problem076():
    """
    It is possible to write five as a sum in exactly six different ways:

       4 + 1
       3 + 2
       3 + 1 + 1
       2 + 2 + 1
       2 + 1 + 1 + 1
       1 + 1 + 1 + 1 + 1

       How many different ways can one hundred be written as a sum of at least
       two positive integers?
    """
    limit = 100
    partitions = []
    for i in range(limit + 1):
        partitions.append([0, ] * (limit + 1))
        for j in reversed(range(limit + 1)):
            if j == i:
                val = 1
            elif j > i:
                val = 0
            elif j == 0:
                val = partitions[i][j + 1]
            else:
                val = partitions[i][j + 1] + partitions[i - j][j]
            partitions[i][j] = val

    ans = partitions[limit][1] - 1
    return ans


if __name__ == "__main__":
    print(problem076())
