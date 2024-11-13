import unittest
from src import rectangle

class RectangleTestCase(unittest.TestCase):
    _test_set = [
        (10, 10, 100, 40),
        (123, 123, 15129, 492),
        (456, 654, 298224, 2220),
        (14, 16, 224, 60),
        (0, 1, ValueError, ValueError),
        (1, 0, ValueError, ValueError),
        (0, 0, ValueError, ValueError),
        (1, -1, ValueError, ValueError),
        (-1, 1, ValueError, ValueError)
    ]

    def test_area(self):
        for case in self._test_set:
            (a, b, ans) = (case[0], case[1], case[2])
            if type(ans) is int:
                self.assertEqual(rectangle.area(a, b), ans, case)
            else:
                with self.assertRaises(ans, msg=case):
                    rectangle.area(a, b)

    def test_perimeter(self):
        for case in self._test_set:
            (a, b, ans) = (case[0], case[1], case[3])
            if type(ans) is int:
                self.assertEqual(rectangle.perimeter(a, b), ans, case)
            else:
                with self.assertRaises(ans, msg=case):
                    rectangle.perimeter(a, b)
