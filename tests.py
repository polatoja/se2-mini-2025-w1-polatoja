import pytest
import random
from functions import func

def test_1():
    assert func("") == 0

def test_2():
    assert func("3") == 3

def test_3():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    input_value = f"{num1},{num2}"
    expected_result = num1 + num2
    assert func(input_value) == expected_result

def test_4():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    input_value = f"{num1}\n{num2}"
    expected_result = num1 + num2
    assert func(input_value) == expected_result

def test_5():
    num1, num2, num3 = random.sample(range(1, 101), 3)
    input_value = f"{num1}\n{num2},{num3}"
    expected_result = num1 + num2 + num3
    assert func(input_value) == expected_result

def test_6():
    with pytest.raises(ValueError):
        func("-3")
    with pytest.raises(ValueError):
        func("3,-4")
    with pytest.raises(ValueError):
        func(f"4\n-5,9")

def test_7():
    assert func("2000") == 0
    assert func(f"4\n1500,9") == 13

def test_8():
    assert func("//#44#5") == 49
    assert func("//a44a6") == 50

def test_9():
    assert func("//[###]44###5###10") == 59
    assert func("//[abba]44abba6") == 50

def test_10():
    assert func("//[###][#]44###5#10") == 59
    assert func("//[abba][#]44#6abba5") == 55