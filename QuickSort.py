# Merges two subarrays of arr[]. 
# First subarray is arr[l..m] 
# Second subarray is arr[m+1..r] 
def merge(arr, leftArrStart, lefArrEnd, rightArrEnd): 
    leftArrSize = lefArrEnd - leftArrStart + 1
    rightArrSize = rightArrEnd- lefArrEnd 
  
    # create temp arrays 
    # Copy data to temp arrays tempLeftArr[] and tempRightArr[] 
    tempLeftArr = [] 
    for leftArrIndex in range(0 , leftArrSize): 
        tempLeftArr.append(arr[leftArrStart + leftArrIndex]) 
  
    tempRightArr = [] 
    for rightArrIndex in range(0 , rightArrSize): 
        tempRightArr.append(arr[lefArrEnd + 1 + rightArrIndex])
  
    # Merge the temp arrays back into arr[l..r] 
    leftArrIndex = 0     # Initial index of first subarray 
    rightArrIndex = 0     # Initial index of second subarray 
    mainArrIndex = leftArrStart     # Initial index of merged subarray 
  
    while leftArrIndex < leftArrSize and rightArrIndex < rightArrSize : 
        if tempLeftArr[leftArrIndex] <= tempRightArr[rightArrIndex]: 
            arr[mainArrIndex] = tempLeftArr[leftArrIndex] 
            leftArrIndex += 1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
        else: 
            arr[mainArrIndex] = tempRightArr[rightArrIndex] 
            rightArrIndex += 1
        mainArrIndex += 1
  
    # Copy the remaining elements of L[], if there 
    # are any 
    while leftArrIndex < leftArrSize: 
        arr[mainArrIndex] = tempLeftArr[leftArrIndex] 
        leftArrIndex += 1
        mainArrIndex += 1
  
    # Copy the remaining elements of R[], if there 
    # are any 
    while rightArrIndex < rightArrSize: 
        arr[mainArrIndex] = tempRightArr[rightArrIndex] 
        rightArrIndex += 1
        mainArrIndex += 1
  
# l is for left index and r is right index of the 
# sub-array of arr to be sorted 
def mergeSort(arr,leftIndex,rightIndex): 
    if leftIndex < rightIndex: 
  
        # Same as (l+r)/2, but avoids overflow for 
        # large l and h 
        Mid = int((leftIndex+(rightIndex-1))/2)
        # Sort first and second halves 
        mergeSort(arr, leftIndex, Mid) 
        mergeSort(arr, Mid+1, rightIndex) 
        merge(arr, leftIndex, Mid, rightIndex) 




ArrayElems = [61, 173, 180, 227, 220, 441, 448, 467, 48, 70, 85, 103, 114, 141, 148, 161, 173, 180, 227, 269, 311, 371, 405, 417]
mergeSort(ArrayElems, 0,len(ArrayElems)-1)
print(ArrayElems)