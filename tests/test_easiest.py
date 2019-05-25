# noinspection PyPackageRequirements
import pytest
from euler_python.easiest import *


def test_smoke():
    print('is it on fire?')


@pytest.mark.fast
def test_sum_multiples_of_3_or_5_below_n():
    n = 10
    output = p001.sum_multiples_of_3_or_5_below_n(n)
    expected_output = 23
    assert output == expected_output


@pytest.mark.slow
def test_problem_1(answer):
    output = p001.problem001()
    expected_output = answer['Problem 001']
    print(' got')
    print(output)
    print(' expected')
    print(expected_output)
    assert output == expected_output


@pytest.mark.fast
def test_sum_even_fib_below():
    output = p002.sum_even_fib_below(90)
    expected_output = 2 + 8 + 34
    assert output == expected_output


@pytest.mark.slow
def test_problem_2(answer):
    output = p002.problem002()
    expected_output = answer['Problem 002']
    assert output == expected_output


@pytest.mark.fast
def test_smallest_prime_factor():
    """
    The prime factors of 13195 are 5, 7, 13 and 29.
    """
    output = p003.smallest_prime_factor(13195)
    expected_output = 5
    assert output == expected_output


@pytest.mark.fast
def test_largest_prime_factor():
    output = p003.largest_prime_factor(13195)
    expected_output = 29
    assert output == expected_output


@pytest.mark.slow
def test_problem_3(answer):
    output = p003.problem003()
    expected_output = answer['Problem 003']
    assert output == expected_output


@pytest.mark.fast
def test_largest_palindrome_from_product_of_two_n_digit_numbers():
    output = p004.largest_palindrome_from_product_of_two_n_digit_numbers(2)
    expected_output = 9009
    assert output == expected_output


@pytest.mark.slow
def test_problem_4(answer):
    output = p004.problem004()
    expected_output = answer['Problem 004']
    assert output == expected_output


def test_problem_5(answer):
    output = p005.problem005()
    expected_output = answer['Problem 005']
    assert output == expected_output


def test_problem_6(answer):
    output = p006.problem006()
    expected_output = answer['Problem 006']
    assert output == expected_output


def test_problem_7(answer):
    output = p007.problem007()
    expected_output = answer['Problem 007']
    assert output == expected_output


def test_problem_8(answer):
    output = p008.problem008()
    expected_output = answer['Problem 008']
    assert output == expected_output


def test_problem_9(answer):
    output = p009.problem009()
    expected_output = answer['Problem 009']
    assert output == expected_output


def test_problem_10(answer):
    output = p010.problem010()
    expected_output = answer['Problem 010']
    assert output == expected_output


def test_problem_11(answer):
    output = p011.problem011()
    expected_output = answer['Problem 011']
    assert output == expected_output


@pytest.mark.slow
def test_problem_12(answer):
    output = p012.problem012()
    expected_output = answer['Problem 012']
    assert output == expected_output


def test_problem_13(answer):
    output = p013.problem013()
    expected_output = answer['Problem 013']
    assert output == expected_output


def test_problem_14(answer):
    output = p014.problem014()
    expected_output = answer['Problem 014']
    assert output == expected_output


def test_problem_15(answer):
    output = p015.problem015()
    expected_output = answer['Problem 015']
    assert output == expected_output


def test_problem_16(answer):
    output = p016.problem016()
    expected_output = answer['Problem 016']
    assert output == expected_output


def test_problem_17(answer):
    output = p017.problem017()
    expected_output = answer['Problem 017']
    assert output == expected_output


def test_problem_18(answer):
    output = p018.problem018()
    expected_output = answer['Problem 018']
    assert output == expected_output


def test_problem_19(answer):
    output = p019.problem019()
    expected_output = answer['Problem 019']
    assert output == expected_output


def test_problem_20(answer):
    output = p020.problem020()
    expected_output = answer['Problem 020']
    assert output == expected_output


def test_problem_21(answer):
    output = p021.problem021()
    expected_output = answer['Problem 021']
    assert output == expected_output


def test_problem_22(answer):
    output = p022.problem022()
    expected_output = answer['Problem 022']
    assert output == expected_output


def test_problem_23(answer):
    output = p023.problem023()
    expected_output = answer['Problem 023']
    assert output == expected_output


def test_problem_24(answer):
    output = p024.problem024()
    expected_output = answer['Problem 024']
    assert output == expected_output


def test_problem_25(answer):
    output = p025.problem025()
    expected_output = answer['Problem 025']
    assert output == expected_output


def test_problem_26(answer):
    output = p026.problem026()
    expected_output = answer['Problem 026']
    assert output == expected_output


@pytest.mark.slow
def test_problem_27(answer):
    output = p027.problem027()
    expected_output = answer['Problem 027']
    assert output == expected_output


def test_problem_28(answer):
    output = p028.problem028()
    expected_output = answer['Problem 028']
    assert output == expected_output


def test_problem_29(answer):
    output = p029.problem029()
    expected_output = answer['Problem 029']
    assert output == expected_output


def test_problem_30(answer):
    output = p030.problem030()
    expected_output = answer['Problem 030']
    assert output == expected_output


def test_problem_31(answer):
    output = p031.problem031()
    expected_output = answer['Problem 031']
    assert output == expected_output


def test_problem_32(answer):
    output = p032.problem032()
    expected_output = answer['Problem 032']
    assert output == expected_output


def test_problem_33(answer):
    output = p033.problem033()
    expected_output = answer['Problem 033']
    assert output == expected_output


def test_problem_34(answer):
    output = p034.problem034()
    expected_output = answer['Problem 034']
    assert output == expected_output


@pytest.mark.slow
def test_problem_35(answer):
    output = p035.problem035()
    expected_output = answer['Problem 035']
    assert output == expected_output


def test_problem_36(answer):
    output = p036.problem036()
    expected_output = answer['Problem 036']
    assert output == expected_output


def test_problem_37(answer):
    output = p037.problem037()
    expected_output = answer['Problem 037']
    assert output == expected_output


def test_problem_38(answer):
    output = p038.problem038()
    expected_output = answer['Problem 038']
    assert output == expected_output


def test_problem_39(answer):
    output = p039.problem039()
    expected_output = answer['Problem 039']
    assert output == expected_output


def test_problem_40(answer):
    output = p040.problem040()
    expected_output = answer['Problem 040']
    assert output == expected_output


@pytest.mark.slow
def test_problem_41(answer):
    output = p041.problem041()
    expected_output = answer['Problem 041']
    assert output == expected_output


def test_problem_42(answer):
    output = p042.problem042()
    expected_output = answer['Problem 042']
    assert output == expected_output


@pytest.mark.slow
def test_problem_43(answer):
    output = p043.problem043()
    expected_output = answer['Problem 043']
    assert output == expected_output


@pytest.mark.slow
def test_problem_44(answer):
    output = p044.problem044()
    expected_output = answer['Problem 044']
    assert output == expected_output


def test_problem_45(answer):
    output = p045.problem045()
    expected_output = answer['Problem 045']
    assert output == expected_output


def test_problem_46(answer):
    output = p046.problem046()
    expected_output = answer['Problem 046']
    assert output == expected_output


def test_problem_47(answer):
    output = p047.problem047()
    expected_output = answer['Problem 047']
    assert output == expected_output


def test_problem_48(answer):
    output = p048.problem048()
    expected_output = answer['Problem 048']
    assert output == expected_output


def test_problem_49(answer):
    output = p049.problem049()
    expected_output = answer['Problem 049']
    assert output == expected_output


def test_problem_50(answer):
    output = p050.problem050()
    expected_output = answer['Problem 050']
    assert output == expected_output


def test_problem_52(answer):
    output = p052.problem052()
    expected_output = answer['Problem 052']
    assert output == expected_output


def test_problem_53(answer):
    output = p053.problem053()
    expected_output = answer['Problem 053']
    assert output == expected_output


def test_problem_55(answer):
    output = p055.problem055()
    expected_output = answer['Problem 055']
    assert output == expected_output


def test_problem_56(answer):
    output = p056.problem056()
    expected_output = answer['Problem 056']
    assert output == expected_output


def test_problem_57(answer):
    output = p057.problem057()
    expected_output = answer['Problem 057']
    assert output == expected_output


def test_problem_58(answer):
    output = p058.problem058()
    expected_output = answer['Problem 058']
    assert output == expected_output


def test_problem_59(answer):
    output = p059.problem059()
    expected_output = answer['Problem 059']
    assert output == expected_output


def test_problem_63(answer):
    output = p063.problem063()
    expected_output = answer['Problem 063']
    assert output == expected_output


def test_problem_67(answer):
    output = p067.problem067()
    expected_output = answer['Problem 067']
    assert output == expected_output


def test_problem_79(answer):
    output = p079.problem079()
    expected_output = answer['Problem 079']
    assert output == expected_output


def test_problem_92(answer):
    output = p092.problem092()
    expected_output = answer['Problem 092']
    assert output == expected_output


def test_problem_97(answer):
    output = p097.problem097()
    expected_output = answer['Problem 097']
    assert output == expected_output

def test_problem_206(answer):
    output = p206.problem206()
    expected_output = answer['Problem 206']
    assert output == expected_output


