from euler_python.utils import eulerlib


def problem051():
    """


    By replacing the 1^st digit of the 2-digit number *3, it turns out that
       six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all
       prime.

       By replacing the 3^rd and 4^th digits of 56**3 with the same digit, this
       5-digit number is the first example having seven primes among the ten
       generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663,
       56773, and 56993. Consequently 56003, being the first member of this
       family, is the smallest prime with this property.

       Find the smallest prime which, by replacing part of the number (not
       necessarily adjacent digits) with the same digit, is part of an eight
       prime value family.
    """
    isprime = eulerlib.list_primality(1000000)
    for i in range(len(isprime)):
        if not isprime[i]:
            continue

        n = [int(c) for c in str(i)]
        for mask in range(1 << len(n)):
            digits = do_mask(n, mask)
            count = 0
            for j in range(10):
                if digits[0] != 0 and isprime[to_number(digits)]:
                    count += 1
                digits = add_mask(digits, mask)

            if count == 8:
                digits = do_mask(n, mask)
                for j in range(10):
                    if digits[0] != 0 and isprime[to_number(digits)]:
                        return to_number(digits)
                    digits = add_mask(digits, mask)
    raise AssertionError("Not found")


def do_mask(digits, mask):
    return [d * ((~mask >> i) & 1) for (i, d) in enumerate(digits)]


def add_mask(digits, mask):
    return [d + ((mask >> i) & 1) for (i, d) in enumerate(digits)]


def to_number(digits):
    result = 0
    for d in digits:
        result = result * 10 + d
    return result


if __name__ == "__main__":
    print(problem051())
