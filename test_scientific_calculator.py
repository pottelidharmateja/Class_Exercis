import unittest
import math

from scientific_calculator import ScientificCalculator

class TestScientificCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = ScientificCalculator()
        
    def test_sin_positive_input(self):
        self.assertAlmostEqual(self.calc.sin(90), 1.0)

    def test_sin_negative_input(self):
        self.assertAlmostEqual(self.calc.sin(-90), -1.0)

    def test_sin_zero_input(self):
        self.assertAlmostEqual(self.calc.sin(0), 0.0)

    def test_sin_non_numeric_input(self):
        with self.assertRaises(TypeError):
            self.calc.sin("hello")

    def test_cos_positive_input(self):
        self.assertAlmostEqual(self.calc.cos(0), 1.0)

    def test_cos_negative_input(self):
        self.assertAlmostEqual(self.calc.cos(-90), 0.0)

    def test_cos_zero_input(self):
        self.assertAlmostEqual(self.calc.cos(90), 0.0)

    def test_cos_non_numeric_input(self):
        with self.assertRaises(TypeError):
            self.calc.cos("hello")

    def test_tan_positive_input(self):
        self.assertAlmostEqual(self.calc.tan(45), 1.0)

    def test_tan_negative_input(self):
        self.assertAlmostEqual(self.calc.tan(-45), -1.0)

    def test_tan_zero_input(self):
        self.assertAlmostEqual(self.calc.tan(0), 0.0)

    def test_tan_non_numeric_input(self):
        with self.assertRaises(TypeError):
            self.calc.tan("hello")

    def test_sqrt_positive_input(self):
        self.assertAlmostEqual(self.calc.sqrt(4), 2.0)

    def test_sqrt_zero_input(self):
        self.assertAlmostEqual(self.calc.sqrt(0), 0.0)

    def test_sqrt_non_positive_input(self):
        with self.assertRaises(ValueError):
            self.calc.sqrt(-1)

    def test_sqrt_non_numeric_input(self):
        with self.assertRaises(TypeError):
            self.calc.sqrt("hello")

    def test_log_positive_input(self):
        self.assertAlmostEqual(self.calc.log(1), 0.0)


    def test_log_zero_input(self):
        with self.assertRaises(ValueError):
            self.calc.log(0)

    def test_log_non_positive_input(self):
        with self.assertRaises(ValueError):
            self.calc.log(-1)

    def test_log_non_numeric_input(self):
        with self.assertRaises(TypeError):
            self.calc.log("hello")

    def test_exp_positive_input(self):
        self.assertAlmostEqual(self.calc.exp(0), 1.0)

    def test_exp_zero_input(self):
        self.assertAlmostEqual(self.calc.exp(0), 1.0)

    def test_exp_negative_input(self):
        self.assertAlmostEqual(self.calc.exp(-1), 1/math.e)

    def test_exp_non_numeric_input(self):
        with self.assertRaises(TypeError):
            self.calc.exp("hello")

if __name__ == "__main__":
    unittest.main()