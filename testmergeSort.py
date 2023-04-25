import time
from mergeSort import MergeSort as MS
import unittest
import matplotlib.pyplot as plt
import numpy as np

class TestMergeSort(unittest.TestCase):

    def genArray(self, size):
        return list(range(size,1,-1))


    def test_mergeSort(self):
        testArray1 = [1,2,3,6,8]
        sortedArray1 = [1,2,3,6,8]
        testArray2 = [11,23,528,536,153,13,5,2,3,5]
        sortedArray2 = [2,3,5,5,11,13,23,153,528,536]
        testArray3 = [7,6,5,4,3,2]
        sortedArray3 = [2,3,4,5,6,7]        
        testArray4 = self.genArray(8)
        sortedArray4 = sorted(testArray4)
        
        
        self.assertEqual(MS(testArray1),sortedArray1)
        self.assertEqual(MS(testArray2),sortedArray2)
        self.assertEqual(MS(testArray3),sortedArray3)
        self.assertEqual(MS(testArray4),sortedArray4)

    def benchmark_mergeSort(self):
        diff = [] 
        for iterator in range(1000,5000,50):
            testArray = self.genArray(iterator)
            initTime = time.time_ns()
            MS(testArray)
            diff.append(time.time_ns() - initTime)
            print(iterator)            
        
        xpoints = np.array(range(1000,5000,50))
        plt.xlabel = "size of array"
        plt.ylabel = "time in ns"
        plt.plot(xpoints, diff)
        plt.show()



            


if __name__ == "__main__":
   testInstance = TestMergeSort()
   testInstance.benchmark_mergeSort()
   unittest.main()
   