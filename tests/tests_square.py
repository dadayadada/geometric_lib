import unittest
from square import area, perimeter

class TestSquare(unittest.TestCase):

    def test_area_positive_side(self):
        self.assertEqual(area(5), 25)
        self.assertEqual(area(10), 100)

    def test_area_zero_side(self):
        self.assertEqual(area(0), 0)

    def test_area_negative_side(self):
        with self.assertRaises(ValueError):
            area(-5)

    def test_perimeter_positive_side(self):
        self.assertEqual(perimeter(5), 20)
        self.assertEqual(perimeter(10), 40)

    def test_perimeter_zero_side(self):
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_negative_side(self):
        with self.assertRaises(ValueError):
            perimeter(-5)

if __name__ == "__main__":
    unittest.main()
