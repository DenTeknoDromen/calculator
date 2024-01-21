import pytest
from application.main import*

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
    assert main("((1+2)+(1+2))×4") == 24
    assert main("(1+2)×(1+2)") == 9
