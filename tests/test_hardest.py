# noinspection PyPackageRequirements
import pytest
from euler_python.hardest import *


def test_problem_331(answer):
    output = p331.problem331()
    expected_output = answer['Problem 331']
    assert output == expected_output


