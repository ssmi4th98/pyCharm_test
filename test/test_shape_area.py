from unittest import TestCase
import src.shape_area as area


class TestshapeArea(TestCase):
    def test_triangle(self):
        self.assertEqual(area.shapeArea.triangle(2, 6), 6)


class TestshapeArea(TestCase):
    def test_rectangle(self):
        self.assertEqual(area.shapeArea.rectangle(6, 2), 12)


class TestshapeArea(TestCase):
    def test_square(self):
        self.assertEqual(area.shapeArea.square(4), 16)