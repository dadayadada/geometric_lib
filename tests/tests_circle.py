import unittest
import math
from circle import area, perimeter


class TestCircle(unittest.TestCase):

    def test_area_positive_radius(self):
        self.assertAlmostEqual(area(5), math.pi * 5 * 5)
        self.assertAlmostEqual(area(10), math.pi * 10 * 10)

    def test_area_zero_radius(self):
        self.assertEqual(area(0), 0)

    def test_area_negative_radius(self):
        with self.assertRaises(ValueError):
            area(-5)

    def test_perimeter_positive_radius(self):
        self.assertAlmostEqual(perimeter(5), 2 * math.pi * 5)
        self.assertAlmostEqual(perimeter(10), 2 * math.pi * 10)

    def test_perimeter_zero_radius(self):
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_negative_radius(self):
        with self.assertRaises(ValueError):
            perimeter(-5)


if __name__ == "__main__":
    unittest.main()
