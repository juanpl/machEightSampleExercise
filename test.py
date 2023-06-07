import unittest
from algorithm import findPair

class TestSum(unittest.TestCase):
    def testNotMatch(self):
        self.assertEqual(findPair([1,2,3,4],12), 'Pair not found')

    def testOnePair(self):
        self.assertEqual(findPair([8,4],12), 'Pair found(8,4)\n')

    def testTwoPair(self):
        self.assertEqual(findPair([8,4,1,11],12), 'Pair found(8,4)\nPair found(1,11)\n')

    def testPairWithZero(self):
        self.assertEqual(findPair([8,4,1,11,0,12],12), 'Pair found(8,4)\nPair found(1,11)\nPair found(0,12)\n')
    
    def testPairWithNegativeValue(self):
        self.assertEqual(findPair([8,4,1,11,0,12,-6,18],12), 'Pair found(8,4)\nPair found(1,11)\nPair found(0,12)\nPair found(-6,18)\n')

if __name__ == '__main__':
    unittest.main()