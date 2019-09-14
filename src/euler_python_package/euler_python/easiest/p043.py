import itertools


def problem043():
    """


    The number, 1406357289, is a 0 to 9 pandigital number because it is made
       up of each of the digits 0 to 9 in some order, but it also has a rather
       interesting sub-string divisibility property.

       Let d[1] be the 1^st digit, d[2] be the 2^nd digit, and so on. In this
       way, we note the following:

         • d[2]d[3]d[4]=406 is divisible by 2
         • d[3]d[4]d[5]=063 is divisible by 3
         • d[4]d[5]d[6]=635 is divisible by 5
         • d[5]d[6]d[7]=357 is divisible by 7
         • d[6]d[7]d[8]=572 is divisible by 11
         • d[7]d[8]d[9]=728 is divisible by 13
         • d[8]d[9]d[10]=289 is divisible by 17

       Find the sum of all 0 to 9 pandigital numbers with this property.
    """
    ans = sum(
        int("".join(map(str, num)))
        for num in itertools.permutations(list(range(10)))
        if is_substring_divisible(num)
    )
    return ans


DIVISIBILITY_TESTS = [2, 3, 5, 7, 11, 13, 17]


def is_substring_divisible(num):
    return all(
        (num[i + 1] * 100 + num[i + 2] * 10 + num[i + 3]) % p == 0
        for (i, p) in enumerate(DIVISIBILITY_TESTS)
    )


if __name__ == "__main__":
    print(problem043())
