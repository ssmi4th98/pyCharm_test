import unittest
from unittest import TestCase
import src.shape_area as area


class TestshapeArea(TestCase):
    def test_triangle(self):
        self.assertEqual(area.shapeArea.triangle(4, 6), 12)

    def test_rectangle(self):
        self.assertEqual(area.shapeArea.rectangle(2, 6), 12)

    @unittest.skip('Skips Test')
    def test_square(self):
        self.assertEqual(area.shapeArea.square(6), 36)

if __name__ == '__main__':

    suite = unittest.makeSuite(TestshapeArea, 'test')
    result = unittest.TextTestRunner(verbosity=2).run(suite)

    print('Errors: ', result.errors)
    print("\nFailures: ", result.failures)
    print("\nSkipped Tests: ", result.skipped)
    print("\nNo. of Tests: ", result.testsRun)
    print("\nWas it a successful test? ", result.wasSuccessful())
