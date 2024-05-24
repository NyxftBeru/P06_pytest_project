from calculator.calculator import Calculator
import pytest

class TestCalculator:
    def test_add(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 5555
        assert result == expected

    def test_subtract(self):
        # arrange
        a = 4321
        b = 123
        cal = Calculator()

        # act
        result = cal.subtract(a, b)

        # assert
        expected = 4198
        assert result == expected

    def test_multiply(self):
        # arrange
        a = 432
        b = 123
        cal = Calculator()

        # act
        result = cal.multiply(a, b)

        # assert
        expected = 53136
        assert result == expected

    def test_divide_not_0(self):
        # arrange
        a = 432
        b = 2
        cal = Calculator()

        # act
        result = cal.divide(a, b)

        # assert
        expected = 216
        assert result == expected

    def test_divide_0(self):
        # arrange
        a = 432
        b = 0
        cal = Calculator()

        # act & assert
        with pytest.raises(ZeroDivisionError):
            cal.divide(a, b)

        
