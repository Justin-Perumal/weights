#!/usr/bin/env python3

import unittest

import bmi


class TestExclude(unittest.TestCase):

    def test_OunceToPound1(self):
        p1 = bmi.ounces2pounds(12)
        self.assertAlmostEqual(p1,0.75)
        
    def test_StoneToPound1(self):
        p1 = bmi.stones2pounds(6)
        self.assertEqual(p1,84)
    	
    def test_PoundsWeight1(self):
        p1 = (bmi.ounces2pounds(12)+13+bmi.stones2pounds(6))
        self.assertAlmostEqual(p1,97.75)
        
    def test_weightKG1(self):
        k1 = bmi.weight2kg(6,13,12)
        self.assertAlmostEqual(k1,44.43181818)
        
    def test_OunceToPound2(self):
        p2 = bmi.ounces2pounds(15)
        self.assertAlmostEqual(p2,0.9375)
        
    def test_StoneToPound2(self):
        p2 = bmi.stones2pounds(10)
        self.assertEqual(p2,140)
    	
    def test_PoundsWeight2(self):
        p2 = (bmi.ounces2pounds(15)+14+bmi.stones2pounds(10))
        self.assertAlmostEqual(p2,154.9375)
        
    def test_weightKG2(self):
        k2 = bmi.weight2kg(10,14,15)
        self.assertAlmostEqual(k2,70.4261363636)
        
if __name__ == '__main__':


    unittest.main()
