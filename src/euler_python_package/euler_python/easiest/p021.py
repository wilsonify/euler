def problem021():
    """


    Let d(n) be defined as the sum of proper divisors of n (numbers less than
       n which divide evenly into n).
       If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair
       and each of a and b are called amicable numbers.

       For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22,
       44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1,
       2, 4, 71 and 142; so d(284) = 220.

     Evaluate the sum of all the amicable numbers under 10000.
    We first compute a table of sum-of-proper-divisors, then we use it to test which numbers are amicable.
    This approach differs from the Java implementation because trying to directly compute
    the proper-divisor-sum of each number by brute force is unacceptably slow in Python.

    """
    # Compute sum of proper divisors for each number
    divisorsum = [0] * 10000
    for i in range(1, len(divisorsum)):
        for j in range(i * 2, len(divisorsum), i):
            divisorsum[j] += i

    # Find all amicable pairs within range
    ans = 0
    for i in range(1, len(divisorsum)):
        j = divisorsum[i]
        if j != i and j < len(divisorsum) and divisorsum[j] == i:
            ans += i
    return ans


if __name__ == "__main__":
    print(problem021())
