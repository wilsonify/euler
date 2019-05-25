import math


def problem074():
    """
    The number 145 is well known for the property that the sum of the
       factorial of its digits is equal to 145:

       1! + 4! + 5! = 1 + 24 + 120 = 145

       Perhaps less well known is 169, in that it produces the longest chain of
       numbers that link back to 169; it turns out that there are only three such
       loops that exist:

       169 → 363601 → 1454 → 169
       871 → 45361 → 871
       872 → 45362 → 872

       It is not difficult to prove that EVERY starting number will eventually
       get stuck in a loop. For example,

       69 → 363600 → 1454 → 169 → 363601 (→ 1454)
       78 → 45360 → 871 → 45361 (→ 871)
       540 → 145 (→ 145)

       Starting with 69 produces a chain of five non-repeating terms, but the
       longest non-repeating chain with a starting number below one million is
       sixty terms.

       How many chains, with a starting number below one million, contain exactly
       sixty non-repeating terms?
    """
    limit = 10 ** 6
    ans = sum(1 for i in range(limit) if get_chain_length(i) == 60)
    return ans


def get_chain_length(n):
    seen = set([])
    while True:
        seen.add(n)
        n = factorialize(n)
        if n in seen:
            return len(seen)


def factorialize(n):
    result = 0
    while n != 0:
        result += FACTORIAL[n % 10]
        n //= 10
    return result


FACTORIAL = [math.factorial(i) for i in range(10)]

if __name__ == "__main__":
    print(problem074())
