def MergeSort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    leftArray = arr[:mid]
    rightArray = arr[mid:]
    
    leftArray = MergeSort(leftArray)
    rightArray = MergeSort(rightArray)
    
    return MERGE(leftArray, rightArray)

def MERGE(leftArray, rightArray):
    result = []
    i = j = 0
    while i < len(leftArray) and j < len(rightArray):
        if leftArray[i] < rightArray[j]:
            result.append(leftArray[i])
            i += 1
        else:
            result.append(rightArray[j])
            j += 1
    
    result += leftArray[i:]
    result += rightArray[j:]
        
    return result


if __name__ == "__main__":
    testArray2 = [11,23,528,536,153,13,5,2,3,5]
    print(MergeSort(testArray2))