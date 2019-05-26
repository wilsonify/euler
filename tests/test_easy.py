"""
test euler_python.easy problems
"""
# noinspection PyPackageRequirements
import pytest


def test_smoke():
    """
    test_smoke()
    :return:
    """
    print('is it on fire?')


@pytest.mark.skip(reason='slow')
def test_problem_51(answer):
    """
    test_problem_51(answer)
    :return:
    """
    from euler_python.easy import p051
    output = p051.problem051()
    expected_output = answer['Problem 051']
    assert output == expected_output


def test_problem_54(answer):
    """
    test_problem_54(answer)
    :return:
    """
    from euler_python.easy import p054
    output = p054.problem054()
    expected_output = answer['Problem 054']
    assert output == expected_output


@pytest.mark.skip(reason='slow')
def test_problem_60(answer):
    """
    test_problem_60(answer)
    :return:
    """
    from euler_python.easy import p060
    output = p060.problem060()
    expected_output = answer['Problem 060']
    assert output == expected_output


def test_problem_61(answer):
    """
    test_problem_61(answer)
    :return:
    """
    from euler_python.easy import p061
    output = p061.problem061()
    expected_output = answer['Problem 061']
    assert output == expected_output


def test_problem_62(answer):
    """
    test_problem_62(answer)
    :return:
    """
    from euler_python.easy import p062
    output = p062.problem062()
    expected_output = answer['Problem 062']
    assert output == expected_output


@pytest.mark.skip(reason='slow')
def test_problem_64(answer):
    """
    test_problem_64(answer)
    :return:
    """
    from euler_python.easy import p064
    output = p064.problem064()
    expected_output = answer['Problem 064']
    assert output == expected_output


def test_problem_65(answer):
    """
    test_problem_65(answer)
    :return:
    """
    from euler_python.easy import p065
    output = p065.problem065()
    expected_output = answer['Problem 065']
    assert output == expected_output


@pytest.mark.skip(reason='slow')
def test_problem_69(answer):
    """
    test_problem_69(answer)
    :return:
    """
    from euler_python.easy import p069
    output = p069.problem069()
    expected_output = answer['Problem 069']
    assert output == expected_output


@pytest.mark.skip(reason='slow')
def test_problem_70(answer):
    """
    test_problem_70(answer)
    :return:
    """
    from euler_python.easy import p070
    output = p070.problem070()
    expected_output = answer['Problem 070']
    assert output == expected_output


def test_problem_71(answer):
    """
    test_problem_71(answer)
    :return:
    """
    from euler_python.easy import p071
    output = p071.problem071()
    expected_output = answer['Problem 071']
    assert output == expected_output


def test_problem_72(answer):
    """
    test_problem_72(answer)
    :return:
    """
    from euler_python.easy import p072
    output = p072.problem072()
    expected_output = answer['Problem 072']
    assert output == expected_output


@pytest.mark.skip(reason='slow')
def test_problem_73(answer):
    """
    test_problem_73(answer)
    :return:
    """
    from euler_python.easy import p073
    output = p073.problem073()
    expected_output = answer['Problem 073']
    assert output == expected_output


@pytest.mark.skip(reason='slow')
def test_problem_74(answer):
    """
    test_problem_74(answer)
    :return:
    """
    from euler_python.easy import p074
    output = p074.problem074()
    expected_output = answer['Problem 074']
    assert output == expected_output


def test_problem_76(answer):
    """
    test_problem_76(answer)
    :return:
    """
    from euler_python.easy import p076
    output = p076.problem076()
    expected_output = answer['Problem 076']
    assert output == expected_output


def test_problem_80(answer):
    """
    test_problem_80(answer)
    :return:
    """
    from euler_python.easy import p080
    output = p080.problem080()
    expected_output = answer['Problem 080']
    assert output == expected_output


def test_problem_81(answer):
    """
    test_problem_81(answer)
    :return:
    """
    from euler_python.easy import p081
    output = p081.problem081()
    expected_output = answer['Problem 081']
    assert output == expected_output


def test_problem_82(answer):
    """
    test_problem_82(answer)
    :return:
    """
    from euler_python.easy import p082
    output = p082.problem082()
    expected_output = answer['Problem 082']
    assert output == expected_output


@pytest.mark.skip(reason='slow')
def test_problem_85(answer):
    """
    test_problem_85(answer)
    :return:
    """
    from euler_python.easy import p085
    output = p085.problem085()
    expected_output = answer['Problem 085']
    assert output == expected_output


def test_problem_87(answer):
    """
    test_problem_87(answer)
    :return:
    """
    from euler_python.easy import p087
    output = p087.problem087()
    expected_output = answer['Problem 087']
    assert output == expected_output


def test_problem_89(answer):
    """
    test_problem_89(answer)
    :return:
    """
    from euler_python.easy import p089
    output = p089.problem089()
    expected_output = answer['Problem 089']
    assert output == expected_output


def test_problem_99(answer):
    """
    test_problem_99(answer)
    :return:
    """
    from euler_python.easy import p099
    output = p099.problem099()
    expected_output = answer['Problem 099']
    assert output == expected_output


def test_problem_102(answer):
    """
    test_problem_102(answer)
    :return:
    """
    from euler_python.easy import p102
    output = p102.problem102()
    expected_output = answer['Problem 102']
    assert output == expected_output


def test_problem_112(answer):
    """
    test_problem_112(answer)
    :return:
    """
    from euler_python.easy import p112
    output = p112.problem112()
    expected_output = answer['Problem 112']
    assert output == expected_output


def test_problem_145(answer):
    """
    test_problem_145(answer)
    :return:
    """
    from euler_python.easy import p145
    output = p145.problem145()
    expected_output = answer['Problem 145']
    assert output == expected_output


def test_problem_205(answer):
    """
    test_problem_205(answer)
    :return:
    """
    from euler_python.easy import p205
    output = p205.problem205()
    expected_output = answer['Problem 205']
    assert output == expected_output


def test_problem_301(answer):
    """
    test_problem_301(answer)
    :return:
    """
    from euler_python.easy import p301
    output = p301.problem301()
    expected_output = answer['Problem 301']
    assert output == expected_output


def test_problem_345(answer):
    """
    test_problem_345(answer)
    :return:
    """
    from euler_python.easy import p345
    output = p345.problem345()
    expected_output = answer['Problem 345']
    assert output == expected_output


def test_problem_346(answer):
    """
    test_problem_346(answer)
    :return:
    """
    from euler_python.easy import p346
    output = p346.problem346()
    expected_output = answer['Problem 346']
    assert output == expected_output


@pytest.mark.skip(reason='slow')
def test_problem_347(answer):
    """
    test_problem_347(answer)
    :return:
    """
    from euler_python.easy import p347
    output = p347.problem347()
    expected_output = answer['Problem 347']
    assert output == expected_output


@pytest.mark.skip(reason='slow')
def test_problem_357(answer):
    """
    test_problem_357(answer)
    :return:
    """
    from euler_python.easy import p357
    output = p357.problem357()
    expected_output = answer['Problem 357']
    assert output == expected_output


@pytest.mark.skip(reason='slow')
def test_problem_381(answer):
    """
    test_problem_381(answer)
    :return:
    """
    from euler_python.easy import p381
    output = p381.problem381()
    expected_output = answer['Problem 381']
    assert output == expected_output


@pytest.mark.skip(reason='slow')
def test_problem_387(answer):
    """
    test_problem_387(answer)
    :return:
    """
    from euler_python.easy import p387
    output = p387.problem387()
    expected_output = answer['Problem 387']
    assert output == expected_output


def test_problem_493(answer):
    """
    test_problem_493(answer)
    :return:
    """
    from euler_python.easy import p493
    output = p493.problem493()
    expected_output = answer['Problem 493']
    assert output == expected_output
