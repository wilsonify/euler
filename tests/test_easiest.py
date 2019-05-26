"""
test the easiest problems
"""
# noinspection PyPackageRequirements
import pytest


def test_smoke():
    """
    test Problem  test_smoke()
    :return:
    """
    print('is it on fire?')


@pytest.mark.fast
def test_sum_multiples_of_3_or_5_below_n():
    """
    test Problem  test_sum_multiples_of_3_or_5_below_n()
    :return:
    """
    input_n = 10
    from euler_python.easiest import p001
    output = p001.sum_multiples_of_3_or_5_below_n(input_n)
    expected_output = 23
    assert output == expected_output


@pytest.mark.skip(reason='slow')
def test_problem_1(answer):
    """
    test Problem  test_problem_1(answer)
    :return:
    """
    from euler_python.easiest import p001
    output = p001.problem001()
    expected_output = answer['Problem 001']
    print(' got')
    print(output)
    print(' expected')
    print(expected_output)
    assert output == expected_output


@pytest.mark.fast
def test_sum_even_fib_below():
    """
    test Problem  test_sum_even_fib_below()
    :return:
    """
    from euler_python.easiest import p002
    output = p002.sum_even_fib_below(90)
    expected_output = 2 + 8 + 34
    assert output == expected_output


@pytest.mark.skip(reason='slow')
def test_problem_2(answer):
    """
    test Problem  test_problem_2(answer)
    :return:
    """
    from euler_python.easiest import p002
    output = p002.problem002()
    expected_output = answer['Problem 002']
    assert output == expected_output


@pytest.mark.fast
def test_smallest_prime_factor():
    """
    test Problem  test_smallest_prime_factor()
    The prime factors of 13195 are 5, 7, 13 and 29.
    :return:
    """
    from euler_python.easiest import p003
    output = p003.smallest_prime_factor(13195)
    expected_output = 5
    assert output == expected_output


@pytest.mark.fast
def test_largest_prime_factor():
    """
    test Problem  test_largest_prime_factor()
    :return:
    """
    from euler_python.easiest import p003
    output = p003.largest_prime_factor(13195)
    expected_output = 29
    assert output == expected_output


@pytest.mark.skip(reason='slow')
def test_problem_3(answer):
    """
    test Problem  test_problem_3(answer)
    :return:
    """
    from euler_python.easiest import p003
    output = p003.problem003()
    expected_output = answer['Problem 003']
    assert output == expected_output


@pytest.mark.fast
def test_largest_palindrome_from_product_of_two_n_digit_numbers():
    """
    test Problem  test_largest_palindrome_from_product_of_two_n_digit_numbers()
    :return:
    """
    from euler_python.easiest import p004
    output = p004.largest_palindrome_from_product_of_two_n_digit_numbers(2)
    expected_output = 9009
    assert output == expected_output


@pytest.mark.skip(reason='slow')
def test_problem_4(answer):
    """
    test Problem  test_problem_4(answer)
    :return:
    """
    from euler_python.easiest import p004
    output = p004.problem004()
    expected_output = answer['Problem 004']
    assert output == expected_output


def test_problem_5(answer):
    """
    test Problem  test_problem_5(answer)
    :return:
    """
    from euler_python.easiest import p005
    output = p005.problem005()
    expected_output = answer['Problem 005']
    assert output == expected_output


def test_problem_6(answer):
    """
    test Problem  test_problem_6(answer)
    :return:
    """
    from euler_python.easiest import p006
    output = p006.problem006()
    expected_output = answer['Problem 006']
    assert output == expected_output


def test_problem_7(answer):
    """
    test Problem  test_problem_7(answer)
    :return:
    """
    from euler_python.easiest import p007
    output = p007.problem007()
    expected_output = answer['Problem 007']
    assert output == expected_output


def test_problem_8(answer):
    """
    test Problem  test_problem_8(answer)
    :return:
    """
    from euler_python.easiest import p008
    output = p008.problem008()
    expected_output = answer['Problem 008']
    assert output == expected_output


def test_problem_9(answer):
    """
    test Problem  test_problem_9(answer)
    :return:
    """
    from euler_python.easiest import p009
    output = p009.problem009()
    expected_output = answer['Problem 009']
    assert output == expected_output


def test_problem_10(answer):
    """
    test Problem  test_problem_10(answer)
    :return:
    """
    from euler_python.easiest import p010
    output = p010.problem010()
    expected_output = answer['Problem 010']
    assert output == expected_output


def test_problem_11(answer):
    """
    test Problem  test_problem_11(answer)
    :return:
    """
    from euler_python.easiest import p011
    output = p011.problem011()
    expected_output = answer['Problem 011']
    assert output == expected_output


def test_triangle_number_factors():
    """
    test Problem  test_problem_12(answer)
    :return:
    """
    from euler_python.easiest import p012
    output = p012.triangle_number_factors(5)
    expected_output = 28
    assert output == expected_output


@pytest.mark.skip(reason='slow')
def test_problem_12(answer):
    """
    test Problem  test_problem_12(answer)
    :return:
    """
    from euler_python.easiest import p012
    output = p012.problem012()
    expected_output = answer['Problem 012']
    assert output == expected_output


def test_problem_13(answer):
    """
    test Problem  test_problem_13(answer)
    :return:
    """
    from euler_python.easiest import p013
    output = p013.problem013()
    expected_output = answer['Problem 013']
    assert output == expected_output


def test_start_collatz_chain():
    """
    test Problem  test_problem_14(answer)
    :return:
    """
    from euler_python.easiest import p014
    output = p014.start_collatz_chain(15)
    expected_output = 9
    assert output == expected_output


@pytest.mark.skip(reason='slow')
def test_problem_14(answer):
    """
    test Problem  test_problem_14(answer)
    :return:
    """
    from euler_python.easiest import p014
    output = p014.problem014()
    expected_output = answer['Problem 014']
    assert output == expected_output


def test_problem_15(answer):
    """
    test Problem  test_problem_15(answer)
    :return:
    """
    from euler_python.easiest import p015
    output = p015.problem015()
    expected_output = answer['Problem 015']
    assert output == expected_output


def test_problem_16(answer):
    """
    test Problem  test_problem_16(answer)
    :return:
    """
    from euler_python.easiest import p016
    output = p016.problem016()
    expected_output = answer['Problem 016']
    assert output == expected_output


def test_problem_17(answer):
    """
    test Problem  test_problem_17(answer)
    :return:
    """
    from euler_python.easiest import p017
    output = p017.problem017()
    expected_output = answer['Problem 017']
    assert output == expected_output


def test_problem_18(answer):
    """
    test Problem  test_problem_18(answer)
    :return:
    """
    from euler_python.easiest import p018
    output = p018.problem018()
    expected_output = answer['Problem 018']
    assert output == expected_output


def test_problem_19(answer):
    """
    test Problem  test_problem_19(answer)
    :return:
    """
    from euler_python.easiest import p019
    output = p019.problem019()
    expected_output = answer['Problem 019']
    assert output == expected_output


def test_problem_20(answer):
    """
    test Problem  test_problem_20(answer)
    :return:
    """
    from euler_python.easiest import p020
    output = p020.problem020()
    expected_output = answer['Problem 020']
    assert output == expected_output


def test_problem_21(answer):
    """
    test Problem  test_problem_21(answer)
    :return:
    """
    from euler_python.easiest import p021
    output = p021.problem021()
    expected_output = answer['Problem 021']
    assert output == expected_output


def test_problem_22(answer):
    """
    test Problem  test_problem_22(answer)
    :return:
    """
    from euler_python.easiest import p022
    output = p022.problem022()
    expected_output = answer['Problem 022']
    assert output == expected_output


@pytest.mark.skip(reason='slow')
def test_problem_23(answer):
    """
    test Problem  test_problem_23(answer)
    :return:
    """
    from euler_python.easiest import p023
    output = p023.problem023()
    expected_output = answer['Problem 023']
    assert output == expected_output


def test_problem_24(answer):
    """
    test Problem  test_problem_24(answer)
    :return:
    """
    from euler_python.easiest import p024
    output = p024.problem024()
    expected_output = answer['Problem 024']
    assert output == expected_output


def test_problem_25(answer):
    """
    test Problem  test_problem_25(answer)
    :return:
    """
    from euler_python.easiest import p025
    output = p025.problem025()
    expected_output = answer['Problem 025']
    assert output == expected_output


def test_problem_26(answer):
    """
    test Problem  test_problem_26(answer)
    :return:
    """
    from euler_python.easiest import p026
    output = p026.problem026()
    expected_output = answer['Problem 026']
    assert output == expected_output


@pytest.mark.skip(reason='slow')
def test_problem_27(answer):
    """
    test Problem  test_problem_27(answer)
    :return:
    """
    from euler_python.easiest import p027
    output = p027.problem027()
    expected_output = answer['Problem 027']
    assert output == expected_output


def test_problem_28(answer):
    """
    test Problem  test_problem_28(answer)
    :return:
    """
    from euler_python.easiest import p028
    output = p028.problem028()
    expected_output = answer['Problem 028']
    assert output == expected_output


def test_problem_29(answer):
    """
    test Problem  test_problem_29(answer)
    :return:
    """
    from euler_python.easiest import p029
    output = p029.problem029()
    expected_output = answer['Problem 029']
    assert output == expected_output


@pytest.mark.skip(reason='slow')
def test_problem_30(answer):
    """
    test Problem  test_problem_30(answer)
    :return:
    """
    from euler_python.easiest import p030
    output = p030.problem030()
    expected_output = answer['Problem 030']
    assert output == expected_output


def test_problem_31(answer):
    """
    test Problem  test_problem_31(answer)
    :return:
    """
    from euler_python.easiest import p031
    output = p031.problem031()
    expected_output = answer['Problem 031']
    assert output == expected_output


def test_problem_32(answer):
    """
    test Problem  test_problem_32(answer)
    :return:
    """
    from euler_python.easiest import p032
    output = p032.problem032()
    expected_output = answer['Problem 032']
    assert output == expected_output


def test_problem_33(answer):
    """
    test Problem  test_problem_33(answer)
    :return:
    """
    from euler_python.easiest import p033
    output = p033.problem033()
    expected_output = answer['Problem 033']
    assert output == expected_output


@pytest.mark.skip(reason='slow')
def test_problem_34(answer):
    """
    test Problem  test_problem_34(answer)
    :return:
    """
    from euler_python.easiest import p034
    output = p034.problem034()
    expected_output = answer['Problem 034']
    assert output == expected_output


@pytest.mark.skip(reason='slow')
def test_problem_35(answer):
    """
    test Problem  test_problem_35(answer)
    :return:
    """
    from euler_python.easiest import p035
    output = p035.problem035()
    expected_output = answer['Problem 035']
    assert output == expected_output


def test_problem_36(answer):
    """
    test Problem  test_problem_36(answer)
    :return:
    """
    from euler_python.easiest import p036
    output = p036.problem036()
    expected_output = answer['Problem 036']
    assert output == expected_output


@pytest.mark.skip(reason='slow')
def test_problem_37(answer):
    """
    test Problem  test_problem_37(answer)
    :return:
    """
    from euler_python.easiest import p037
    output = p037.problem037()
    expected_output = answer['Problem 037']
    assert output == expected_output


def test_problem_38(answer):
    """
    test Problem  test_problem_38(answer)
    :return:
    """
    from euler_python.easiest import p038
    output = p038.problem038()
    expected_output = answer['Problem 038']
    assert output == expected_output


@pytest.mark.skip(reason='slow')
def test_problem_39(answer):
    """
    test Problem  test_problem_39(answer)
    :return:
    """
    from euler_python.easiest import p039
    output = p039.problem039()
    expected_output = answer['Problem 039']
    assert output == expected_output


def test_problem_40(answer):
    """
    test Problem  test_problem_40(answer)
    :return:
    """
    from euler_python.easiest import p040
    output = p040.problem040()
    expected_output = answer['Problem 040']
    assert output == expected_output


@pytest.mark.skip(reason='slow')
def test_problem_41(answer):
    """
    test Problem  test_problem_41(answer)
    :return:
    """
    from euler_python.easiest import p041
    output = p041.problem041()
    expected_output = answer['Problem 041']
    assert output == expected_output


def test_problem_42(answer):
    """
    test Problem  test_problem_42(answer)
    :return:
    """
    from euler_python.easiest import p042
    output = p042.problem042()
    expected_output = answer['Problem 042']
    assert output == expected_output


@pytest.mark.skip(reason='slow')
def test_problem_43(answer):
    """
    test Problem  test_problem_43(answer)
    :return:
    """
    from euler_python.easiest import p043
    output = p043.problem043()
    expected_output = answer['Problem 043']
    assert output == expected_output


@pytest.mark.skip(reason='slow')
def test_problem_44(answer):
    """
    test Problem  test_problem_44(answer)
    :return:
    """
    from euler_python.easiest import p044
    output = p044.problem044()
    expected_output = answer['Problem 044']
    assert output == expected_output


def test_problem_45(answer):
    """
    test Problem  test_problem_45(answer)
    :return:
    """
    from euler_python.easiest import p045
    output = p045.problem045()
    expected_output = answer['Problem 045']
    assert output == expected_output


def test_problem_46(answer):
    """
    test Problem  test_problem_46(answer)
    :return:
    """
    from euler_python.easiest import p046
    output = p046.problem046()
    expected_output = answer['Problem 046']
    assert output == expected_output


@pytest.mark.skip(reason='slow')
def test_problem_47(answer):
    """
    test Problem  test_problem_47(answer)
    :return:
    """
    from euler_python.easiest import p047
    output = p047.problem047()
    expected_output = answer['Problem 047']
    assert output == expected_output


def test_problem_48(answer):
    """
    test Problem  test_problem_48(answer)
    :return:
    """
    from euler_python.easiest import p048
    output = p048.problem048()
    expected_output = answer['Problem 048']
    assert output == expected_output


def test_problem_49(answer):
    """
    test Problem  test_problem_49(answer)
    :return:
    """
    from euler_python.easiest import p049
    output = p049.problem049()
    expected_output = answer['Problem 049']
    assert output == expected_output


def test_problem_50(answer):
    """
    test Problem  test_problem_50(answer)
    :return:
    """
    from euler_python.easiest import p050
    output = p050.problem050()
    expected_output = answer['Problem 050']
    assert output == expected_output


def test_problem_52(answer):
    """
    test Problem  test_problem_52(answer)
    :return:
    """
    from euler_python.easiest import p052
    output = p052.problem052()
    expected_output = answer['Problem 052']
    assert output == expected_output


def test_problem_53(answer):
    """
    test Problem  test_problem_53(answer)
    :return:
    """
    from euler_python.easiest import p053
    output = p053.problem053()
    expected_output = answer['Problem 053']
    assert output == expected_output


def test_problem_55(answer):
    """
    test Problem  test_problem_55(answer)
    :return:
    """
    from euler_python.easiest import p055
    output = p055.problem055()
    expected_output = answer['Problem 055']
    assert output == expected_output


def test_problem_56(answer):
    """
    test Problem  test_problem_56(answer)
    :return:
    """
    from euler_python.easiest import p056
    output = p056.problem056()
    expected_output = answer['Problem 056']
    assert output == expected_output


def test_problem_57(answer):
    """
    test Problem  test_problem_57(answer)
    :return:
    """
    from euler_python.easiest import p057
    output = p057.problem057()
    expected_output = answer['Problem 057']
    assert output == expected_output


@pytest.mark.skip(reason='slow')
def test_problem_58(answer):
    """
    test Problem  test_problem_58(answer)
    :return:
    """
    from euler_python.easiest import p058
    output = p058.problem058()
    expected_output = answer['Problem 058']
    assert output == expected_output


@pytest.mark.skip(reason='slow')
def test_problem_59(answer):
    """
    test Problem  test_problem_59(answer)
    :return:
    """
    from euler_python.easiest import p059
    output = p059.problem059()
    expected_output = answer['Problem 059']
    assert output == expected_output


def test_problem_63(answer):
    """
    test Problem  test_problem_63(answer)
    :return:
    """
    from euler_python.easiest import p063
    output = p063.problem063()
    expected_output = answer['Problem 063']
    assert output == expected_output


def test_problem_67(answer):
    """
    test Problem  test_problem_67(answer)
    :return:
    """
    from euler_python.easiest import p067
    output = p067.problem067()
    expected_output = answer['Problem 067']
    assert output == expected_output


@pytest.mark.skip(reason='slow')
def test_problem_79(answer):
    """
    test Problem  test_problem_79(answer)
    :return:
    """
    from euler_python.easiest import p079
    output = p079.problem079()
    expected_output = answer['Problem 079']
    assert output == expected_output


@pytest.mark.skip(reason='slow')
def test_problem_92(answer):
    """
    test Problem  test_problem_92(answer)
    :return:
    """
    from euler_python.easiest import p092
    output = p092.problem092()
    expected_output = answer['Problem 092']
    assert output == expected_output


def test_problem_97(answer):
    """
    test Problem  test_problem_97(answer)
    :return:
    """
    from euler_python.easiest import p097
    output = p097.problem097()
    expected_output = answer['Problem 097']
    assert output == expected_output


@pytest.mark.skip(reason='slow')
def test_problem_206(answer):
    """
    test Problem  test_problem_206(answer)
    :return:
    """
    from euler_python.easiest import p206
    output = p206.problem206()
    expected_output = answer['Problem 206']
    assert output == expected_output
