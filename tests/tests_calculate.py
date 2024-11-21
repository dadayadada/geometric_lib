import unittest
import math
import circle
import square
from calculate import calc


class TestCalc(unittest.TestCase):

    def test_circle_perimeter(self):
        result = calc("circle", "perimeter", [5])
        self.assertAlmostEqual(result, 2 * math.pi * 5)

    def test_circle_area(self):
        result = calc("circle", "area", [5])
        self.assertAlmostEqual(result, math.pi * 5 * 5)

    def test_square_perimeter(self):
        result = calc("square", "perimeter", [5])
        self.assertEqual(result, 4 * 5)

    def test_square_area(self):
        result = calc("square", "area", [5])
        self.assertEqual(result, 5 * 5)

    def test_invalid_figure(self):
        with self.assertRaises(AssertionError):
            calc("triangle", "perimeter", [5])

    def test_invalid_function(self):
        with self.assertRaises(AssertionError):
            calc("circle", "volume", [5])

    def test_invalid_size(self):
        with self.assertRaises(TypeError):
            calc("circle", "perimeter", [5, 10])

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            calc("circle", "perimeter", [-5])
        with self.assertRaises(ValueError):
            calc("circle", "area", [-5])

    def test_negative_side(self):
        with self.assertRaises(ValueError):
            calc("square", "perimeter", [-5])
        with self.assertRaises(ValueError):
            calc("square", "area", [-5])


if __name__ == "__main__":
    unittest.main()
