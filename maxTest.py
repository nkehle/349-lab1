# CSC 349-01, Fall 2023)
# Noa Kehle and Andrew Okerlund
# Lab 1


import numpy as np
import findMax
import unittest
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')


def compareCount():
    testArr = [5, 10, 50, 100, 200, 1000]
    repeats = 25
    avgLinear = []
    avgDNC = []
    avgLinearTmp = 0
    avgDNCTmp = 0

    for i in testArr:
        for j in range(1, repeats):
            arr = np.random.randint(1, 100, i)
            avgLinearTmp += findMax.findSecondLinearWithCount(arr)[1]
            avgDNCTmp += findMax.findSecondDNCWithCount(arr)[1]

        avgLinear.append(avgLinearTmp / repeats)
        avgDNC.append(avgDNCTmp / repeats)

    return testArr, avgLinear, avgDNC


# gather results
res = compareCount()

# plot linear
plt.plot(res[0], res[1], label='findSecondLinear', color='blue', linestyle='-')

# plot dnc
plt.plot(res[0], res[2], label='findSecondDNC ', color='red', linestyle='--')

# labels
plt.xlabel('Length of the Array')
plt.ylabel('Average number of comparisons')
plt.title('Avg number of comparisons to find second largest sizes')
plt.grid = True
plt.legend()

# show plotting
plt.show()

# Unit Tests Used
''' 
class Tests(unittest.TestCase):

    def testFindMaxLinear(self):
        arr = np.array([31, 7, 48, 1, 5, 19, 2, 26, 52, 3, 95])
        max = findMax.findMaxLinear(arr)
        self.assertEqual(max, 95)

    def testFindMaxLinearWithCount(self):
        arr = np.array([31, 7, 48, 1, 5, 19, 2, 26, 52, 3, 95])
        max = findMax.findMaxLinearWithCount(arr)
        self.assertEqual(max[1], 10)

    def testFindMaxDNC(self):
        arr = np.array([31, 7, 48, 1, 5, 19, 2, 26, 52, 3, 95])
        max = findMax.findMaxDNC(arr, 0, len(arr) - 1)
        self.assertEqual(max, 95)

    def testFindMaxDNCWithCount(self):
        arr = np.array([31, 7, 48, 1, 5, 19, 2, 26, 52, 3, 95])
        max = findMax.findMaxDNCWithCount(arr, 0, len(arr) - 1)
        self.assertEqual(max[1], 10)

    def testFindSecondLinear(self):
        arr = np.array([31, 7, 48, 1, 5, 19, 2, 26, 52, 3, 95])
        max = findMax.findSecondLinear(arr)
        self.assertEqual(max, 52)

    def testFindSecondLinearWithCount(self):
        arr = np.array([31, 7, 48, 1, 5, 19, 2, 26, 52, 3, 95])
        max = findMax.findSecondLinearWithCount(arr)
        self.assertEqual(max[1], 10)

    def testFindSecondDNC(self):
        arr = np.array([31, 7, 48, 1, 5, 19, 2, 26, 52, 3, 95])
        max = findMax.findSecondDNC(arr)
        self.assertEqual(max, 52)
'''
