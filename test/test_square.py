import unittest
from src import square

class SquareTestCase(unittest.TestCase):
    # (a, area, perimeter)
    _test_set = [
        (10, 100, 40),
        (123, 15129, 492),
        (456, 207936, 1824),
        (14, 196, 56),
        (5.432, 29.506624, 21.728),
        (0, ValueError, ValueError),
        (-1, ValueError, ValueError)
    ]

    def test_area(self):
        for case in self._test_set:
            (a, ans) = (case[0], case[1])
            if type(ans) is int:
                self.assertEqual(square.area(a), ans, case)
            elif type(ans) is float:
                self.assertAlmostEqual(square.area(a), ans, msg=case)
            else:
                with self.assertRaises(ans, msg=case):
                    square.area(a)

    def test_perimeter(self):
        for case in self._test_set:
            (a, ans) = (case[0], case[2])
            if type(ans) is int:
                self.assertEqual(square.perimeter(a), ans, case)
            elif type(ans) is float:
                self.assertAlmostEqual(square.perimeter(a), ans, msg=case)
            else:
                with self.assertRaises(ans, msg=case):
                    square.perimeter(a)
