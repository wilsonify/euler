from euler_python.utils import eulerlib


def problem381():
    """


    For a prime p let S(p) = (∑(p-k)!) mod(p) for 1 ≤ k ≤ 5.

       For example, if p=7,
       (7-1)! + (7-2)! + (7-3)! + (7-4)! + (7-5)! = 6! + 5! + 4! + 3! + 2! =
       720+120+24+6+2 = 872.
       As 872 mod(7) = 4, S(7) = 4.

       It can be verified that ∑S(p) = 480 for 5 ≤ p < 100.

       Find ∑S(p) for 5 ≤ p < 10^8.

    # Note about the mathematical simplification:
    # (p-5)! + (p-4)! + (p-3)! + (p-2)! + (p-1)!
    # = (p-5)! * (1 + (p-4) + (p-4)(p-3) + (p-4)(p-3)(p-2) + (p-4)(p-3)(p-2)(p-1))
    # = (p-5)! * (1 + (-4) + (-4)(-3) + (-4)(-3)(-2) + (-4)(-3)(-2)(-1))
    # = (p-5)! * (1 + -4 + 12 + -24 + 24)
    # = (p-5)! * 9
    # = (p-1)! / ((p-1)(p-2)(p-3)(p-4)) * 9
    # = (p-1)! / ((-1)(-2)(-3)(-4)) * 9
    # = (p-1)! / 24 * 9
    # = (p-1)! * (3 * 3) / (3 * 8)
    # = (p-1)! * 3 / 8
    # = -1 * 3 / 8  (by Wilson's theorem)
    # = -3/8 mod p.
    # Every part of the equation is modulo a prime p > 4.
    """

    def s(p):
        return (p - 3) * eulerlib.reciprocal_mod(8 % p, p) % p

    ans = sum(s(p) for p in eulerlib.prime_generator(10 ** 8) if p >= 5)
    return ans


if __name__ == "__main__":
    print(problem381())
