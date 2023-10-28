import unittest
from Solver import solver

#
class solver_tests(unittest.TestCase):
    def test_linear(self):
        expected_text = 'Линейное уравнение\n x = %s\n' % (-1.0)
        self.assertEqual(solver(0, 0, 1, 1), expected_text)

    def test_quadratic_with_same_real_roots(self):
        expected_text = 'Квадратное уравнение\n x1 = %s\n x2 = %s\n' % (-1.0, -1.0)
        self.assertEqual(solver(0, 1, 2, 1), expected_text)

    def test_quadratic_with_different_real_roots(self):
        expected_text = 'Квадратное уравнение\n x1 = %s\n x2 = %s\n' % (-1.0, -2.0)
        self.assertEqual(solver(0, 1, 3, 2), expected_text)

    def test_quadratic_with_non_real_roots(self):
        expected_text = 'Квадратное уравнение\n x1 = %s\n x2 = %s\n' % ('-0.5+0.866i', '-0.5-0.866i')
        self.assertEqual(solver(0, 1, 1, 1), expected_text)

    def test_cubic_with_same_real_roots(self):
        expected_text = 'Кубическое уравнение\n x1 = %s\n x2 = %s\n x3 = %s\n' % (-1.0, -1.0, -1.0)
        self.assertEqual(solver(1, 3, 3, 1), expected_text)

    def test_cubic_with_different_real_roots(self):
        expected_text = 'Кубическое уравнение\n x1 = %s\n x2 = %s\n x3 = %s\n' % (4.2, -2.0, 1.0)
        self.assertEqual(solver(1, -3.2, -6.2, 8.4), expected_text)

    def test_cubic_with_one_real_and_two_non_real_roots(self):
        expected_text = 'Кубическое уравнение\n x1 = %s\n x2 = %s\n x3 = %s\n' % (-1.0, '1i', '-1i')
        self.assertEqual(solver(1, 1, 1, 1), expected_text)
