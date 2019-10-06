import unittest
import sys
from math import sqrt

from homework import Rectangle


class TestCases(unittest.TestCase):

    def tested_values(self):
        self.test_Rectangle1 = Rectangle(2.5, 5)
        self.test_Rectangle2 = Rectangle(2,)

    def test_get_rectangle_perimeter_1_valid_values(self):
        self.assertEqual(self.test_Rectangle1.get_rectangle_perimeter(), 15)

    def test_get_rectangle_perimeter_2_empty_sides(self):
        self.assertIsNone(self.test_Rectangle2.get_rectangle_perimeter())

    def test_get_rectangle_square_1_valid_values(self):
        self.assertEqual(self.test_Rectangle1.get_rectangle_square(), 12.5)

    def test_get_rectangle_square_2_empty_sides(self):
        self.assertIsNone(self.test_Rectangle2.get_rectangle_square())

    def test_get_sum_of_corners_0_to_3(self):
        for i in range(4):
            self.assertEqual(self.test_Rectangle1.get_sum_of_corners(i), i*90)

    def test_get_sum_of_corners_4_more(self):
        for i in range(5, sys.maxsize):
            self.assertRaises(ValueError, self.test_Rectangle1.get_sum_of_corners(i))

    def test_get_rectangle_diagonal_1_valid_values(self):
        self.assertAlmostEqual(self.test_Rectangle1.get_rectangle_diagonal(), sqrt(31.25))
        self.assertAlmostEqual(self.test_Rectangle2.get_rectangle_diagonal(), sqrt(4))

    def test_get_radius_of_circumscribed_circle(self):
        self.assertAlmostEqual(self.test_Rectangle1.get_radius_of_circumscribed_circle(), sqrt(31.25)/2)

    def test_get_radius_of_inscribed_circle_valid_values(self):
        result = test_Rectangle1.get_radius_of_inscribed_circle() / 2 * sqrt(2)
        self.assertEqual(self.test_Rectangle1.get_radius_of_inscribed_circle(), result)

    def test_get_radius_of_inscribed_circle_equality(self):
        if Rectangle.width == Rectangle.height:
            self.assertRaises(ValueError, self.test_Rectangle1.get_radius_of_inscribed_circle)


if __name__ == '__main__':
    unittest.main()















