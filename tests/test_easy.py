"""
test easy problems
"""
# noinspection PyPackageRequirements
import pytest

from euler_python import easy


def test_smoke():
    """
    test_smoke()
    :return:
    """
    print('is it on fire?')


@pytest.mark.slow
def test_problem_51(answer):
    """
    test_problem_51(answer)
    :return:
    """
    output = easy.p051.problem051()
    expected_output = answer['Problem 051']
    assert output == expected_output


def test_problem_54(answer):
    """
    test_problem_54(answer)
    :return:
    """
    output = easy.p054.problem054()
    expected_output = answer['Problem 054']
    assert output == expected_output


def test_problem_60(answer):
    """
    test_problem_60(answer)
    :return:
    """
    output = easy.p060.problem060()
    expected_output = answer['Problem 060']
    assert output == expected_output


def test_problem_61(answer):
    """
    test_problem_61(answer)
    :return:
    """
    output = easy.p061.problem061()
    expected_output = answer['Problem 061']
    assert output == expected_output


def test_problem_62(answer):
    """
    test_problem_62(answer)
    :return:
    """
    output = easy.p062.problem062()
    expected_output = answer['Problem 062']
    assert output == expected_output


def test_problem_64(answer):
    """
    test_problem_64(answer)
    :return:
    """
    output = easy.p064.problem064()
    expected_output = answer['Problem 064']
    assert output == expected_output


def test_problem_65(answer):
    """
    test_problem_65(answer)
    :return:
    """
    output = easy.p065.problem065()
    expected_output = answer['Problem 065']
    assert output == expected_output


def test_problem_69(answer):
    """
    test_problem_69(answer)
    :return:
    """
    output = easy.p069.problem069()
    expected_output = answer['Problem 069']
    assert output == expected_output


def test_problem_70(answer):
    """
    test_problem_70(answer)
    :return:
    """
    output = easy.p070.problem070()
    expected_output = answer['Problem 070']
    assert output == expected_output


def test_problem_71(answer):
    """
    test_problem_71(answer)
    :return:
    """
    output = easy.p071.problem071()
    expected_output = answer['Problem 071']
    assert output == expected_output


def test_problem_72(answer):
    """
    test_problem_72(answer)
    :return:
    """
    output = easy.p072.problem072()
    expected_output = answer['Problem 072']
    assert output == expected_output


def test_problem_73(answer):
    """
    test_problem_73(answer)
    :return:
    """
    output = easy.p073.problem073()
    expected_output = answer['Problem 073']
    assert output == expected_output


def test_problem_74(answer):
    """
    test_problem_74(answer)
    :return:
    """
    output = easy.p074.problem074()
    expected_output = answer['Problem 074']
    assert output == expected_output


def test_problem_76(answer):
    """
    test_problem_76(answer)
    :return:
    """
    output = easy.p076.problem076()
    expected_output = answer['Problem 076']
    assert output == expected_output


def test_problem_80(answer):
    """
    test_problem_80(answer)
    :return:
    """
    output = easy.p080.problem080()
    expected_output = answer['Problem 080']
    assert output == expected_output


def test_problem_81(answer):
    """
    test_problem_81(answer)
    :return:
    """
    output = easy.p081.problem081()
    expected_output = answer['Problem 081']
    assert output == expected_output


def test_problem_82(answer):
    """
    test_problem_82(answer)
    :return:
    """
    output = easy.p082.problem082()
    expected_output = answer['Problem 082']
    assert output == expected_output


def test_problem_85(answer):
    """
    test_problem_85(answer)
    :return:
    """
    output = easy.p085.problem085()
    expected_output = answer['Problem 085']
    assert output == expected_output


def test_problem_87(answer):
    """
    test_problem_87(answer)
    :return:
    """
    output = easy.p087.problem087()
    expected_output = answer['Problem 087']
    assert output == expected_output


def test_problem_89(answer):
    """
    test_problem_89(answer)
    :return:
    """
    output = easy.p089.problem089()
    expected_output = answer['Problem 089']
    assert output == expected_output


def test_problem_99(answer):
    """
    test_problem_99(answer)
    :return:
    """
    output = easy.p099.problem099()
    expected_output = answer['Problem 099']
    assert output == expected_output


def test_problem_102(answer):
    """
    test_problem_102(answer)
    :return:
    """
    output = easy.p102.problem102()
    expected_output = answer['Problem 102']
    assert output == expected_output


def test_problem_112(answer):
    """
    test_problem_112(answer)
    :return:
    """
    output = easy.p112.problem112()
    expected_output = answer['Problem 112']
    assert output == expected_output


def test_problem_145(answer):
    """
    test_problem_145(answer)
    :return:
    """
    output = easy.p145.problem145()
    expected_output = answer['Problem 145']
    assert output == expected_output


def test_problem_205(answer):
    """
    test_problem_205(answer)
    :return:
    """
    output = easy.p205.problem205()
    expected_output = answer['Problem 205']
    assert output == expected_output


def test_problem_301(answer):
    """
    test_problem_301(answer)
    :return:
    """
    output = easy.p301.problem301()
    expected_output = answer['Problem 301']
    assert output == expected_output


def test_problem_345(answer):
    """
    test_problem_345(answer)
    :return:
    """
    output = easy.p345.problem345()
    expected_output = answer['Problem 345']
    assert output == expected_output


def test_problem_346(answer):
    """
    test_problem_346(answer)
    :return:
    """
    output = easy.p346.problem346()
    expected_output = answer['Problem 346']
    assert output == expected_output


def test_problem_347(answer):
    """
    test_problem_347(answer)
    :return:
    """
    output = easy.p347.problem347()
    expected_output = answer['Problem 347']
    assert output == expected_output


def test_problem_357(answer):
    """
    test_problem_357(answer)
    :return:
    """
    output = easy.p357.problem357()
    expected_output = answer['Problem 357']
    assert output == expected_output


def test_problem_381(answer):
    """
    test_problem_381(answer)
    :return:
    """
    output = easy.p381.problem381()
    expected_output = answer['Problem 381']
    assert output == expected_output


def test_problem_387(answer):
    """
    test_problem_387(answer)
    :return:
    """
    output = easy.p387.problem387()
    expected_output = answer['Problem 387']
    assert output == expected_output


def test_problem_493(answer):
    """
    test_problem_493(answer)
    :return:
    """
    output = easy.p493.problem493()
    expected_output = answer['Problem 493']
    assert output == expected_output
