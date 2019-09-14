from euler_python.utils import eulerlib


def problem231():
    N = 20000000
    K = 15000000
    smallestprimefactor = eulerlib.list_smallest_prime_factors(N)

    def factorial_prime_factor_sum(n):
        result = 0
        for i in range(n + 1):
            j = i
            while j > 1:
                p = smallestprimefactor[j]
                result += p
                j //= p
        return result

    ans = (
            factorial_prime_factor_sum(N)
            - factorial_prime_factor_sum(K)
            - factorial_prime_factor_sum(N - K)
    )
    return ans


if __name__ == "__main__":
    print(problem231())
