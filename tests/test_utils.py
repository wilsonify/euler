# noinspection PyPackageRequirements
import pytest
from euler_python.utils import eulerlib


@pytest.mark.parametrize(
    "input_x,expected_output", [
        (10, 2),
        (100, 3),
        (450180, 10)])
def test_popcount(input_x, expected_output):
    output = eulerlib.popcount(input_x)
    print(output)
    assert output == expected_output


@pytest.mark.parametrize(
    "input_x,expected_output", [
        (9, 3),
        (25, 5),
        (625, 25)])
def test_sqrt(input_x, expected_output):
    output = eulerlib.sqrt(input_x)
    print(output)
    assert output == expected_output


@pytest.mark.parametrize(
    "input_x,expected_output", [
        (9, True),
        (10, False),
        (25, True),
        (625, True),
        (626, False)])
def test_is_square(input_x, expected_output):
    output = eulerlib.is_square(input_x)
    print(output)
    assert output == expected_output


@pytest.mark.parametrize(
    "input_x,expected_output", [
        (0, False),
        (1, False),
        (2, True),
        (7, True),
        (626, False)])
def test_is_prime(input_x, expected_output):
    output = eulerlib.is_prime(input_x)
    print(output)
    assert output == expected_output


@pytest.mark.parametrize(
    "input_n,expected_output", [
        (9, [False, False, True,
             True, False, True,
             False, True, False, False]),
        (25, [False, False, True, True, False,
              True, False, True, False, False,
              False, True, False, True, False,
              False, False, True, False, True,
              False, False, False, True, False, False])])
def test_list_primality(input_n, expected_output):
    output = eulerlib.list_primality(input_n)
    print(output)
    assert output == expected_output


@pytest.mark.parametrize(
    "input_n,expected_output", [
        (9, [2, 3, 5, 7]),
        (10, [2, 3, 5, 7]),
        (25, [2, 3, 5, 7, 11, 13, 17, 19, 23])])
def test_list_primes(input_n, expected_output):
    output = eulerlib.list_primes(input_n)
    print(output)
    assert output == expected_output


@pytest.mark.parametrize(
    "limit,expected_output", [
        (9, [2, 3, 5, 7]),
        (10, [2, 3, 5, 7]),
        (25, [2, 3, 5, 7, 11, 13, 17, 19, 23]),
        (626,
         [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107,
          109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229,
          233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359,
          367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491,
          499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619])])
def test_prime_generator(limit, expected_output):
    output = [_ for _ in eulerlib.prime_generator(limit)]
    print(output)
    assert output == expected_output


@pytest.mark.parametrize(
    "input_n,expected_output", [
        (9, [None, None, 2, 3, 2, 5, 2, 7, 2, 3]),
        (10, [None, None, 2, 3, 2, 5, 2, 7, 2, 3, 2]),
        (25, [None, None, 2, 3, 2, 5, 2, 7, 2, 3, 2, 11, 2, 13, 2, 3, 2, 17, 2, 19, 2, 3, 2, 23, 2, 5]),
        (625,
         [None, None, 2, 3, 2, 5, 2, 7, 2, 3, 2, 11, 2, 13, 2, 3, 2, 17, 2, 19, 2, 3, 2, 23, 2, 5, 2, 3, 2, 29, 2, 31,
          2, 3, 2, 5, 2, 37, 2, 3, 2, 41, 2, 43, 2, 3, 2, 47, 2, 7, 2, 3, 2, 53, 2, 5, 2, 3, 2, 59, 2, 61, 2, 3, 2, 5,
          2, 67, 2, 3, 2, 71, 2, 73, 2, 3, 2, 7, 2, 79, 2, 3, 2, 83, 2, 5, 2, 3, 2, 89, 2, 7, 2, 3, 2, 5, 2, 97, 2, 3,
          2, 101, 2, 103, 2, 3, 2, 107, 2, 109, 2, 3, 2, 113, 2, 5, 2, 3, 2, 7, 2, 11, 2, 3, 2, 5, 2, 127, 2, 3, 2, 131,
          2, 7, 2, 3, 2, 137, 2, 139, 2, 3, 2, 11, 2, 5, 2, 3, 2, 149, 2, 151, 2, 3, 2, 5, 2, 157, 2, 3, 2, 7, 2, 163,
          2, 3, 2, 167, 2, 13, 2, 3, 2, 173, 2, 5, 2, 3, 2, 179, 2, 181, 2, 3, 2, 5, 2, 11, 2, 3, 2, 191, 2, 193, 2, 3,
          2, 197, 2, 199, 2, 3, 2, 7, 2, 5, 2, 3, 2, 11, 2, 211, 2, 3, 2, 5, 2, 7, 2, 3, 2, 13, 2, 223, 2, 3, 2, 227, 2,
          229, 2, 3, 2, 233, 2, 5, 2, 3, 2, 239, 2, 241, 2, 3, 2, 5, 2, 13, 2, 3, 2, 251, 2, 11, 2, 3, 2, 257, 2, 7, 2,
          3, 2, 263, 2, 5, 2, 3, 2, 269, 2, 271, 2, 3, 2, 5, 2, 277, 2, 3, 2, 281, 2, 283, 2, 3, 2, 7, 2, 17, 2, 3, 2,
          293, 2, 5, 2, 3, 2, 13, 2, 7, 2, 3, 2, 5, 2, 307, 2, 3, 2, 311, 2, 313, 2, 3, 2, 317, 2, 11, 2, 3, 2, 17, 2,
          5, 2, 3, 2, 7, 2, 331, 2, 3, 2, 5, 2, 337, 2, 3, 2, 11, 2, 7, 2, 3, 2, 347, 2, 349, 2, 3, 2, 353, 2, 5, 2, 3,
          2, 359, 2, 19, 2, 3, 2, 5, 2, 367, 2, 3, 2, 7, 2, 373, 2, 3, 2, 13, 2, 379, 2, 3, 2, 383, 2, 5, 2, 3, 2, 389,
          2, 17, 2, 3, 2, 5, 2, 397, 2, 3, 2, 401, 2, 13, 2, 3, 2, 11, 2, 409, 2, 3, 2, 7, 2, 5, 2, 3, 2, 419, 2, 421,
          2, 3, 2, 5, 2, 7, 2, 3, 2, 431, 2, 433, 2, 3, 2, 19, 2, 439, 2, 3, 2, 443, 2, 5, 2, 3, 2, 449, 2, 11, 2, 3, 2,
          5, 2, 457, 2, 3, 2, 461, 2, 463, 2, 3, 2, 467, 2, 7, 2, 3, 2, 11, 2, 5, 2, 3, 2, 479, 2, 13, 2, 3, 2, 5, 2,
          487, 2, 3, 2, 491, 2, 17, 2, 3, 2, 7, 2, 499, 2, 3, 2, 503, 2, 5, 2, 3, 2, 509, 2, 7, 2, 3, 2, 5, 2, 11, 2, 3,
          2, 521, 2, 523, 2, 3, 2, 17, 2, 23, 2, 3, 2, 13, 2, 5, 2, 3, 2, 7, 2, 541, 2, 3, 2, 5, 2, 547, 2, 3, 2, 19, 2,
          7, 2, 3, 2, 557, 2, 13, 2, 3, 2, 563, 2, 5, 2, 3, 2, 569, 2, 571, 2, 3, 2, 5, 2, 577, 2, 3, 2, 7, 2, 11, 2, 3,
          2, 587, 2, 19, 2, 3, 2, 593, 2, 5, 2, 3, 2, 599, 2, 601, 2, 3, 2, 5, 2, 607, 2, 3, 2, 13, 2, 613, 2, 3, 2,
          617, 2, 619, 2, 3, 2, 7, 2, 5])])
def test_list_smallest_prime_factors(input_n, expected_output):
    output = eulerlib.list_smallest_prime_factors(input_n)
    print(output)
    assert output == expected_output


@pytest.mark.parametrize(
    "input_n,expected_output", [
        (9, [0, 1, 1, 2, 2, 4, 2, 6, 4, 6]),
        (10, [0, 1, 1, 2, 2, 4, 2, 6, 4, 6, 4]),
        (25, [0, 1, 1, 2, 2, 4, 2, 6, 4, 6, 4, 10, 4, 12, 6, 8, 8, 16, 6, 18, 8, 12, 10, 22, 8, 20])])
def test_list_totients(input_n, expected_output):
    output = eulerlib.list_totients(input_n)
    print(output)
    assert output == expected_output


@pytest.mark.parametrize(
    "input_n, input_k,expected_output", [
        (9, 1, 9),
        (10, 2, 45),
        (25, 5, 53130),
        (626, 1, 626)])
def test_binomial(input_n, input_k, expected_output):
    output = eulerlib.binomial(input_n, input_k)
    print(output)
    assert output == expected_output


@pytest.mark.parametrize(
    "input_x,input_m,expected_output", [
        (19, 23, 17), ])
def test_reciprocal_mod(input_x, input_m, expected_output):
    output = eulerlib.reciprocal_mod(input_x, input_m)
    print(output)
    assert output == expected_output


@pytest.mark.parametrize(
    "input_arr,expected_output", [([9, 10], True)])
def test_next_permutation(input_arr, expected_output):
    output = eulerlib.next_permutation(input_arr)
    print(output)
    assert output == expected_output
