
import itertools


def problem095():
    """


    The proper divisors of a number are all the divisors excluding the number
       itself. For example, the proper divisors of 28 are 1, 2, 4, 7, and 14. As
       the sum of these divisors is equal to 28, we call it a perfect number.

       Interestingly the sum of the proper divisors of 220 is 284 and the sum of
       the proper divisors of 284 is 220, forming a chain of two numbers. For
       this reason, 220 and 284 are called an amicable pair.

       Perhaps less well known are longer chains. For example, starting with
       12496, we form a chain of five numbers:

                 12496 → 14288 → 15472 → 14536 → 14264 (→ 12496 → ...)

       Since this chain returns to its starting point, it is called an amicable
       chain.

       Find the smallest member of the longest amicable chain with no element
       exceeding one million.
    """

    LIMIT = 10 ** 6

    # divisorsum[n] is the sum of all the proper divisors of n
    divisorsum = [0] * (LIMIT + 1)
    for i in range(1, LIMIT + 1):
        for j in range(i * 2, LIMIT + 1, i):
            divisorsum[j] += i

    # Analyze the amicable chain length for each number in ascending order
    maxchainlen = 0
    ans = -1
    for i in range(LIMIT + 1):
        visited = set()
        cur = i
        for count in itertools.count(1):
            # 'count' is the length of the this amicable chain
            visited.add(cur)
            next = divisorsum[cur]
            if next == i:
                if count > maxchainlen:
                    ans = i
                    maxchainlen = count
                break
            # Exceeds limit or not a chain (a rho shape instead)
            elif next > LIMIT or next in visited:
                break
            else:
                cur = next

    return ans


if __name__ == "__main__":
    print(problem095())
