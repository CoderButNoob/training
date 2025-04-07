import pytest
from source import my_function

def test_add():
    result = my_function.add(1,4)
    assert result == 5

def test_divide():
    result = my_function.divide(10,5)
    assert result == 2

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        my_function.divide(10,0)

def test_add_str():
    result = my_function.add("I like " , "Burger")
    assert result == "I like Burger"

    