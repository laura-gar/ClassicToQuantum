import unittest
from LAB import*

class MyTestCase(unittest.TestCase):
    def test_classicToQuantum(self):
        m = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,1,0,0,0,1],[0,0,0,1,0,0],[0,0,1,0,0,0],[1,0,0,0,1,0]]
        v = [6,2,1,5,3,10]
        self.assertEqual(clasToQuan(m,v,1),[0,0,12,5,1,9])

    def test_multiplesRendijas(self):
        self.assertEqual(expRendijas(2,5,2),[0.0, 0.0, 0.0, 0.17, 0.17, 0.34, 0.17, 0.17])

    def test_expQuatum(self):
        self.assertEqual(expQuantic(2,5,2),[(0.0, 0.0), (0.0, 0.0), (0.0, 0.0), (-0.288, 0.288), (-0.288, -0.288), (0.0, 0.0), (-0.288, -0.288), (0.288, -0.288)])


if __name__ == '__main__':
    unittest.main()
