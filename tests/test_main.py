import pytest
from application.main import*

# def test_make_float():
#     assert type(make_float(5)) == float
#     assert type(make_float(5.5)) == float
#     assert type(make_float(-15)) == float
#     assert make_float("banan") ==  None

# def test_get_operand():
#     nums = [10, 5]
#     assert get_operand(nums, "+") == 15
#     nums = [-10, -5]
#     assert get_operand(nums, "+") == -15
#     nums = [10.5, 5.5]
#     assert get_operand(nums, "+") == 16

#     nums = [10, 5]
#     assert get_operand(nums, "-") == 5
#     nums = [-10, -5]
#     assert get_operand(nums, "-") == -5
#     nums = [10.5, 5.5]
#     assert get_operand(nums, "-") == 5

#     nums = [10, 5]
#     assert get_operand(nums, "*") == 50
#     nums = [-10, -5]
#     assert get_operand(nums, "*") == 50
#     nums = [10.5, 5.5]
#     assert get_operand(nums, "*") == 57.75

#     nums = [10, 5]
#     assert get_operand(nums, "/") == 2
#     nums = [-10, -5]
#     assert get_operand(nums, "/") == 2
#     nums = [40.8, 20.4]
#     assert get_operand(nums, "/") == 2

#     nums = [10, 5]
#     assert get_operand(nums, "**") == 100000
#     nums = [-10, -5]
#     assert get_operand(nums, "**") == -0.00001

#     nums = [36, 3]
#     assert get_operand(nums, "%") == 0

def test_main():
    assert main("1+2×3") == 7
    assert main("(1+2)×3") == 9
    assert main("5×5×5") == 125
    assert main("7×7×7") == 343

    assert main("0.1+0.2") == 0.3
    assert main("0.4-0.3") == 0.1
    assert main("0.4+0.3") == 0.7
    assert main("0.4×0.2") == 0.08
    assert main("(0.4-0.3)+(0.1+0.2)") == 0.4
    assert main("(0.4×0.6)") == 0.24

    assert main("1+8÷2") == 5

    assert main("3+5^2") == 28
    assert main("3×5^2") == 75

    assert main("(5×5)+(5×5)") == 50
    assert main("(-5)+9") == 4
    assert main("(-5)+(-5)") == -10
    assert main("+5-3") == 2
    assert main("π×π") == 9.869604401089358
    assert main("5×5×π") == 78.53981633974483
    assert main("7×7×π") == 153.93804002589985
    assert main("+5-3-") == 2
    assert main("((1+2)+(1+2))*4") == 24
