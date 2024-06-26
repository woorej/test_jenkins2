import pytest
    
@pytest.mark.parametrize("num1, num2, expected_result",[
    (1, 2, 3),
    (2, 3, 5)
])
def test_add(cal, num1, num2, expected_result):
    assert expected_result == cal.add(num1, num2)
    
@pytest.mark.parametrize("num1, num2, expected_result",[
    (1, 2, -1),
    (2, 3, -1)
])
def test_subtract(cal, num1, num2, expected_result):
    assert expected_result == cal.subtract(num1, num2)