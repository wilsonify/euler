def problem063():
    """
    The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the
       9-digit number, 134217728=8^9, is a ninth power.

       How many n-digit positive integers exist which are also an nth power?

    Let's examine n^k for different values of n and k and see which
    choices cannot possibly work (i.e. not being exactly k digits long).

    When n = 10, for each k, n^k has exactly k+1 digits, so these are excluded.
    By extension, when n > 10, for each k, n^k has at least k+1 digits, so these are excluded.
    Thus we should only consider 1 <= n <= 9.

    When n = 9, k = 22, then n^k has 21 digits which is insufficient.
    Extending this, when n = 9 and k > 22, n^k has fewer than k digits.
    Furthermore, when n < 9, n^k will have start to have
    fewer than k digits at some value of k with k < 22.
    Therefore we should only consider 1 <= k <= 21.

    We handle the rest of the testing by brute force.

    """
    ans = sum(1
              for i in range(1, 10)
              for j in range(1, 22)
              if len(str(i ** j)) == j)
    return ans


if __name__ == "__main__":
    print(problem063())
