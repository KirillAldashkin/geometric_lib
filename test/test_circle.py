import unittest
from src import circle
from math import pi, sqrt

class CircleTestCase(unittest.TestCase):
    # (r, area, perimeter)
    _test_set = [
        (1, pi, 2 * pi),
        (3, 9 * pi, 6 * pi),
        (7 / pi, 49 / pi, 14.0),
        (5 / sqrt(pi), 25.0, 10 * sqrt(pi)),
        (0, ValueError, ValueError),
        (-1, ValueError, ValueError)
    ]

    def test_area(self):
        for case in self._test_set:
            (r, ans) = (case[0], case[1])
            if type(ans) is int:
                self.assertEqual(circle.area(r), ans, case)
            elif type(ans) is float:
                self.assertAlmostEqual(circle.area(r), ans, msg=case)
            else:
                with self.assertRaises(ans, msg=case):
                    circle.area(r)

    def test_perimeter(self):
        for case in self._test_set:
            (r, ans) = (case[0], case[2])
            if type(ans) is int:
                self.assertEqual(circle.perimeter(r), ans, case)
            elif type(ans) is float:
                self.assertAlmostEqual(circle.perimeter(r), ans, msg=case)
            else:
                with self.assertRaises(ans, msg=case):
                    circle.perimeter(r)
