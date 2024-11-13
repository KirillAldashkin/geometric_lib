import unittest
from src import triangle
from math import sqrt

class TriangleTestCase(unittest.TestCase):
    # (a, b, c, h, area, perimeter)
    _test_set = [
      (5, 4, 3, 2.4, 6, 12),
      (2, 2, 2, sqrt(3), sqrt(3), 6),
      (25, 20, 15, 12, 150, 60),
      (0, 20, 15, 12, ValueError, ValueError),
      (25, 0, 15, 12, 150, ValueError),
      (25, 20, 0, 12, 150, ValueError),
      (25, 20, 15, 0, ValueError, 60)
    ]

    def test_area(self):
        for case in self._test_set:
            (a, h, ans) = (case[0], case[3], case[4])
            if type(ans) is int:
                self.assertEqual(triangle.area(a, h), ans, case)
            elif type(ans) is float:
                self.assertAlmostEqual(triangle.area(a, h), ans, msg=case)
            else:
                with self.assertRaises(ans, msg=case):
                    triangle.area(a, h)

    def test_perimeter(self):
        for case in self._test_set:
            (a, b, c, ans) = (case[0], case[1], case[2], case[5])
            if type(ans) is int:
                self.assertEqual(triangle.perimeter(a, b, c), ans, case)
            elif type(ans) is float:
                self.assertAlmostEqual(triangle.perimeter(a, b, c), ans, msg=case)
            else:
                with self.assertRaises(ans, msg=case):
                    triangle.perimeter(a, b, c)
