import pytest
from application.main import*

def test_make_float():
    assert type(make_float(5)) == float
    assert type(make_float(5.5)) == float
    assert type(make_float(-15)) == float
    assert make_float("banan") ==  None

def test_get_operand():
    nums = [10, 5]
    assert get_operand(nums, "+") == 15
    nums = [-10, -5]
    assert get_operand(nums, "+") == -15
    nums = [10.5, 5.5]
    assert get_operand(nums, "+") == 16

    nums = [10, 5]
    assert get_operand(nums, "-") == 5
    nums = [-10, -5]
    assert get_operand(nums, "-") == -5
    nums = [10.5, 5.5]
    assert get_operand(nums, "-") == 5

    nums = [10, 5]
    assert get_operand(nums, "*") == 50
    nums = [-10, -5]
    assert get_operand(nums, "*") == 50
    nums = [10.5, 5.5]
    assert get_operand(nums, "*") == 57.75

    nums = [10, 5]
    assert get_operand(nums, "/") == 2
    nums = [-10, -5]
    assert get_operand(nums, "/") == 2
    nums = [40.8, 20.4]
    assert get_operand(nums, "/") == 2

    nums = [10, 5]
    assert get_operand(nums, "**") == 100000
    nums = [-10, -5]
    assert get_operand(nums, "**") == -0.00001

    nums = [36, 3]
    assert get_operand(nums, "%") == 0
