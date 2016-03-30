import unittest
from exerciseC4S1Q1 import MaxSubarrayImplementations

class FindMaxSubarrayTests(unittest.TestCase):

    def testMaximumSubarrayBFOneElement(self):
        findMax = MaxSubarrayImplementations()
        result = findMax.maximumSubarrayBF([3], 0, 0)
        self.failUnless(result == (0, 0, 3)) 

    def testMaximumSubarrayBFSmArray(self):
        findMax = MaxSubarrayImplementations()
        array = [0, 1, -4, 3, -4]
        result = findMax.maximumSubarrayBF(array, 0, 4)
        self.failUnless(result == (3, 3, 3))

    def testMaximumSubarrayBFLgArray(self):
        findMax = MaxSubarrayImplementations()
        array = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
        result = findMax.maximumSubarrayBF(array, 0, 15)
        self.failUnless(result == (7, 10, 43))

    def testMaxCrossingSubarayOne(self):
        findMax = MaxSubarrayImplementations()
        result = findMax.findMaxCrossingSubarray([-3], 0, 0, 0)
        print result
        self.failUnless(result == (0, 0, -3))
        #fails bc returns -inf; fix the test or code? 

    def testMaxCrossingSubaraySm(self):
        findMax = MaxSubarrayImplementations()
        array = [-23, 18, 20]
        result = findMax.findMaxCrossingSubarray(array, 0, 1, 2)
        self.failUnless(result == (0, 2, 15))

    def testMaxCrossingSubarayLrg(self):
        findMax = MaxSubarrayImplementations()
        array = [-3, 2, 4, -1, 2, -4]
        result = findMax.findMaxCrossingSubarray(array, 0, 3, 5)
        self.failUnless(result == (1, 4, 7))

    def testMaximumSubarrayRecBase(self):
        findMax = MaxSubarrayImplementations()
        result = findMax.maximumSubarrayRec([3], 0, 0)
        self.failUnless(result == (0, 0, 3))

    def testMaximumSubarrayRecSm(self):
        findMax = MaxSubarrayImplementations()
        array = [0, 1, -4, 3, -4]
        result = findMax.maximumSubarrayRec(array, 0,4)
        self.failUnless(result == (3, 3, 3))

    def testMaximumSubarrayRecLrg(self):
        findMax = MaxSubarrayImplementations()
        array = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
        result = findMax.maximumSubarrayBF(array, 0, 15)
        self.failUnless(result == (7, 10, 43))

#class FindMaxSubarrayTests(unittest.TestCase):
#tests for helpers needs to test randomness :)

def main():
    unittest.main()

if __name__ == '__main__':
    main()