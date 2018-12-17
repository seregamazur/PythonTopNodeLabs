import unittest

from PythonTopNodeLabs.Lab6_1 import half_per
from PythonTopNodeLabs.Lab6_1 import calculate
from PythonTopNodeLabs.Lab6_1 import input_ui


class Test(unittest.TestCase):
    def test_half_per(self):
        self.assertEqual(half_per(4, 9, 10), 11.5)
        self.assertAlmostEqual(half_per(4, 9, 10), 11.5000000000002)
        self.assertNotEqual(half_per(-11,0,9),0)
        self.assertNotEqual(half_per(-11,5,0),1)
        self.assertRaises(Exception,half_per(11/5.0,1,10))
    def test_calculate(self):
        self.assertAlmostEqual(calculate(4,9,10),17.9843682)
        self.assertEqual(calculate(4,9,10),17.984368212422698)
        self.assertRaises(Exception,calculate(11, 2, 9), 0)
        self.assertAlmostEqual(calculate(12,2,10),0)
        self.assertEqual(calculate(12, 2, 10), 0.0)
        self.assertEqual(calculate(12, 2, 10), 0)
    def test_input_ui(self):
        self.assertEqual(input_ui(),2,4,6)
        self.assertEqual(input_ui(), 4, 2, 6)
