import sys
from src import math_func
import pytest


# @pytest.mark.number
# @pytest.mark.skip(reason="do not run this test")
# @pytest.mark.skipif(sys.version_info < (3, 7), reason="do not run this test")
def test_add():
    assert math_func.add(7, 3) == 10
    assert math_func.add(7) == 9
    print("-> printing .....", math_func.add(7, 3))


# @pytest.mark.number
def test_product():
    assert math_func.product(5, 5) == 25
    assert math_func.product(5) == 10


# @pytest.mark.strings
def test_add_strings():
    result = math_func.add('Hello', ' World')
    assert result == 'Hello World'
    assert type(result) is str
    assert 'Hello' in result


# @pytest.mark.strings
def test_product_strings():
    assert math_func.product('Hello ', 3) == 'Hello Hello Hello '
    result = math_func.product('Hello ')
    assert result == 'Hello Hello '
    assert type(result) is str
    assert 'Hello' in result


# @pytest.mark.parametrize(
#     'num1,num2,result',
#     [
#         (7, 3, 10),
#         ("Hello ", "World", "Hello World"),
#         (10.5, 25.5, 36)
#     ]
# )
# def test_add(num1, num2, result):
#     assert math_func.add(num1, num2) == result
