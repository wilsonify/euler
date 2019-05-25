
from euler_python.utils import eulerlib


def problem204():
    LIMIT = 10 ** 9
    primes = eulerlib.list_primes(100)

    def count(primeindex, product):
        if primeindex == len(primes):
            return 1 if product <= LIMIT else 0
        else:
            result = 0
            while product <= LIMIT:
                result += count(primeindex + 1, product)
                product *= primes[primeindex]
            return result

    return (count(0, 1))


if __name__ == "__main__":
    print(problem204())
