import unittest
from LAB import*

class MyTestCase(unittest.TestCase):
    def test_classicToQuantum(self):
        m = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,1,0,0,0,1],[0,0,0,1,0,0],[0,0,1,0,0,0],[1,0,0,0,1,0]]
        v = [6,2,1,5,3,10]
        self.assertEqual(clasToQuan(m,v,1),[0,0,12,5,1,9])

    def test_multiplesRendijas(self):
        self.assertEqual(expRendijas(3,7,4),[0.0, 0.0, 0.0, 0.0, 0.11, 0.11, 0.22, 0.11, 0.22, 0.11, 0.11])

    def test_expQuatum(self):
        self.assertEqual(expQuantic(3,7,1),[(0, 0), (0.577, 0.0), (0.577, 0.0), (0.577, 0.0), (0.0, 0.0), (0.0, 0.0), (0.0, 0.0), (0.0, 0.0), (0.0, 0.0), (0.0, 0.0), (0.0, 0.0)])


if __name__ == '__main__':
    unittest.main()
