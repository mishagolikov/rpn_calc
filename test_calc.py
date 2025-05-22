import unittest
from calc import RPNCalculator

class TestRPNCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = RPNCalculator()

    def test_addition(self):
        self.calc.evaluate(["5", "8", "+"])
        self.assertAlmostEqual(self.calc.stack[-1], 13.0)

    def test_subtraction(self):
        self.calc.evaluate(["10", "4", "-"])
        self.assertAlmostEqual(self.calc.stack[-1], 6.0)

    def test_multiplication(self):
        self.calc.evaluate(["-3", "-2", "*"])
        self.assertAlmostEqual(self.calc.stack[-1], 6.0)

    def test_division(self):
        self.calc.evaluate(["5", "8", "/"])
        self.assertAlmostEqual(self.calc.stack[-1], 0.625)

    def test_complex(self):
        self.calc.evaluate(["5", "5", "5", "8", "+", "+", "-"])
        self.assertAlmostEqual(self.calc.stack[-1], -13.0)

if __name__ == '__main__':
    unittest.main()
