import time
from insertionSort import insertionSort as IS
import unittest
import matplotlib.pyplot as plt
import numpy as np

class TestInsertionSort(unittest.TestCase):

    def genArray(self, size):
        return list(range(size,1,-1))


    def test_insertionSort(self):
        testArray1 = [1,2,3,6,8]
        sortedArray1 = [1,2,3,6,8]
        testArray2 = [11,23,528,536,153,13,5,2,3,5]
        sortedArray2 = [2,3,5,5,11,13,23,153,528,536]
        testArray3 = [7,6,5,4,3,2]
        sortedArray3 = [2,3,4,5,6,7]        
        testArray4 = self.genArray(8)
        sortedArray4 = sorted(testArray4)
        
        IS(testArray1)
        IS(testArray2)
        IS(testArray3)
        IS(testArray4)
        
        self.assertEqual(testArray1,sortedArray1)
        self.assertEqual(testArray2,sortedArray2)
        self.assertEqual(testArray3,sortedArray3)
        self.assertEqual(testArray4,sortedArray4)

    def benchmark_insertionSort(self):
        diff = [] 
        for iterator in range(1000,5000,50):
            testArray = self.genArray(iterator)
            initTime = time.time_ns()
            IS(testArray)
            diff.append(time.time_ns() - initTime)
            print(iterator)            
        
        xpoints = np.array(range(1000,5000,50))
        plt.xlabel = "size of array"
        plt.ylabel = "time in ns"
        plt.plot(xpoints, diff)
        plt.show()



            


if __name__ == "__main__":
   #unittest.main()
   testInstance = TestInsertionSort()
   testInstance.benchmark_insertionSort()
