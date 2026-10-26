"""Unit tests covering the original and graded calculator operations."""

from pathlib import Path
import sys
import unittest

SOURCE_ROOT = Path(__file__).resolve().parents[3] / "src" / "main" / "python"
sys.path.insert(0, str(SOURCE_ROOT))

from calculator_Natalio_Hassoun import (  # noqa: E402
    add,
    divide,
    modulus,
    multiply,
    power,
    square_root,
    subtract,
)


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)

    def test_add_negative(self):
        self.assertEqual(add(-5, 2), -3)

    def test_add_decimal(self):
        self.assertAlmostEqual(add(0.1, 0.2), 0.3)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_subtract_negative_result(self):
        self.assertEqual(subtract(3, 5), -2)

    def test_subtract_equal_values(self):
        self.assertEqual(subtract(7, 7), 0)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_multiply_by_zero(self):
        self.assertEqual(multiply(8, 0), 0)

    def test_multiply_negative(self):
        self.assertEqual(multiply(-3, 4), -12)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_fractional_result(self):
        self.assertAlmostEqual(divide(7, 2), 3.5)

    def test_divide_zero_numerator(self):
        self.assertEqual(divide(0, 5), 0)

    def test_divide_by_zero(self):
        with self.assertRaisesRegex(ValueError, "Cannot divide by zero"):
            divide(10, 0)

    def test_modulus(self):
        self.assertEqual(modulus(10, 3), 1)

    def test_modulus_exact_multiple(self):
        self.assertEqual(modulus(12, 4), 0)

    def test_modulus_zero_numerator(self):
        self.assertEqual(modulus(0, 3), 0)

    def test_modulus_negative_dividend(self):
        self.assertEqual(modulus(-10, 3), 2)

    def test_modulus_negative_divisor(self):
        self.assertEqual(modulus(10, -3), -2)

    def test_modulus_decimal(self):
        self.assertAlmostEqual(modulus(5.5, 2), 1.5)

    def test_modulus_by_zero(self):
        with self.assertRaisesRegex(ValueError, "zero divisor"):
            modulus(10, 0)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)

    def test_power_zero_exponent(self):
        self.assertEqual(power(7, 0), 1)

    def test_power_negative_exponent(self):
        self.assertAlmostEqual(power(2, -2), 0.25)

    def test_power_negative_base(self):
        self.assertEqual(power(-2, 3), -8)

    def test_power_fractional_exponent(self):
        self.assertAlmostEqual(power(9, 0.5), 3)

    def test_power_zero_to_zero(self):
        self.assertEqual(power(0, 0), 1)

    def test_power_zero_to_negative(self):
        with self.assertRaises(ZeroDivisionError):
            power(0, -1)

    def test_square_root(self):
        self.assertEqual(square_root(16), 4)

    def test_square_root_zero(self):
        self.assertEqual(square_root(0), 0)

    def test_square_root_one(self):
        self.assertEqual(square_root(1), 1)

    def test_square_root_non_perfect_square(self):
        self.assertAlmostEqual(square_root(2), 2 ** 0.5)

    def test_square_root_decimal(self):
        self.assertAlmostEqual(square_root(0.25), 0.5)

    def test_square_root_negative(self):
        with self.assertRaisesRegex(ValueError, "negative number"):
            square_root(-1)


if __name__ == "__main__":
    unittest.main()
