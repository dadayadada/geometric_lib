import unittest
from triangle import area, perimeter


class TestTriangle(unittest.TestCase):

    def test_area_positive_sides(self):
        self.assertAlmostEqual(area(3, 4, 5), 6)
        self.assertAlmostEqual(area(6, 8, 10), 24)

    def test_area_zero_sides(self):
        with self.assertRaises(ValueError):
            area(0, 4, 5)
        with self.assertRaises(ValueError):
            area(3, 0, 5)
        with self.assertRaises(ValueError):
            area(3, 4, 0)

    def test_area_negative_sides(self):
        with self.assertRaises(ValueError):
            area(-3, 4, 5)
        with self.assertRaises(ValueError):
            area(3, -4, 5)
        with self.assertRaises(ValueError):
            area(3, 4, -5)

    def test_area_invalid_triangle(self):
        with self.assertRaises(ValueError):
            area(1, 1, 3)
        with self.assertRaises(ValueError):
            area(1, 3, 1)
        with self.assertRaises(ValueError):
            area(3, 1, 1)

    def test_perimeter_positive_sides(self):
        self.assertEqual(perimeter(3, 4, 5), 12)
        self.assertEqual(perimeter(6, 8, 10), 24)

    def test_perimeter_zero_sides(self):
        with self.assertRaises(ValueError):
            perimeter(0, 4, 5)
        with self.assertRaises(ValueError):
            perimeter(3, 0, 5)
        with self.assertRaises(ValueError):
            perimeter(3, 4, 0)

    def test_perimeter_negative_sides(self):
        with self.assertRaises(ValueError):
            perimeter(-3, 4, 5)
        with self.assertRaises(ValueError):
            perimeter(3, -4, 5)
        with self.assertRaises(ValueError):
            perimeter(3, 4, -5)

    def test_perimeter_invalid_triangle(self):
        with self.assertRaises(ValueError):
            perimeter(1, 1, 3)
        with self.assertRaises(ValueError):
            perimeter(1, 3, 1)
        with self.assertRaises(ValueError):
            perimeter(3, 1, 1)


if __name__ == "__main__":
    unittest.main()
