import itertools


def problem044():
    """


    Pentagonal numbers are generated by the formula, P[n]=n(3n−1)/2. The first
       ten pentagonal numbers are:

                      1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

       It can be seen that P[4] + P[7] = 22 + 70 = 92 = P[8]. However, their
       difference, 70 − 22 = 48, is not pentagonal.

       Find the pair of pentagonal numbers, P[j] and P[k], for which their sum
       and difference are pentagonal and D = |P[k] − P[j]| is minimised; what is
       the value of D?
    """
    pentanum = PentagonalNumberHelper()
    min_d = None  # None means not found yet, positive number means found a candidate
    # For each upper pentagonal number index, going upward
    for i in itertools.count(2):
        pent_i = pentanum.term(i)
        # If the next number down is at least as big as a found difference, then conclude searching
        if min_d is not None and pent_i - pentanum.term(i - 1) >= min_d:
            break

        # For each lower pentagonal number index, going downward
        for j in range(i - 1, 0, -1):
            pent_j = pentanum.term(j)
            diff = pent_i - pent_j
            # If the difference is at least as big as a found difference, then stop testing lower pentagonal numbers
            if min_d is not None and diff >= min_d:
                break
            elif pentanum.is_term(pent_i + pent_j) and pentanum.is_term(diff):
                min_d = diff  # Found a smaller difference
    return min_d


# Provides memoization for generating and testing pentagonal numbers.
class PentagonalNumberHelper(object):
    def __init__(self):
        self.term_list = [0]
        self.term_set = set()

    def term(self, x):
        assert x > 0
        while len(self.term_list) <= x:
            n = len(self.term_list)
            term = (n * (n * 3 - 1)) >> 1
            self.term_list.append(term)
            self.term_set.add(term)
        return self.term_list[x]

    def is_term(self, y):
        assert y > 0
        while self.term_list[-1] < y:
            n = len(self.term_list)
            term = (n * (n * 3 - 1)) >> 1
            self.term_list.append(term)
            self.term_set.add(term)
        return y in self.term_set


if __name__ == "__main__":
    print(problem044())
