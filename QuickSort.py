def midPoint(len):
    if(len%2 ==0):
        return int(len/2 -1)
    else:
        return int(len/2)

def quickSort(arr,pivotLoc,leftStart,rightEnd):
    tempLeftArray  = []
    tempRightArray = []

    if(leftStart >= pivotLoc):
        return

    iCnt = leftStart
    midValue = arr[pivotLoc]
    while(iCnt <= rightEnd):
        if(iCnt == pivotLoc):
            iCnt = iCnt+1
            continue
        assert iCnt < len(arr)
        if(arr[iCnt] <= midValue):
            tempLeftArray.append(arr[iCnt])
        else:
            tempRightArray.append(arr[iCnt])
        
        iCnt = iCnt+1
    
    tempLeftArray.append(midValue)

    iCnt = 0
    for iCnt in range(0,len(tempLeftArray)):
        arr[leftStart + iCnt] = tempLeftArray[iCnt]

    iCnt = 0
    for iCnt in range(0,len(tempRightArray)):
        arr[leftStart+len(tempLeftArray)+ iCnt] = tempRightArray[iCnt]


    print(arr)

    tempLeftStart = leftStart
    tempLeftPivot = midPoint(len(tempLeftArray))
    tempLeftRightEnd = len(tempLeftArray)-1
    quickSort(arr,tempLeftPivot,tempLeftStart, tempLeftRightEnd)
    
    tempRightStart = tempLeftRightEnd+1
    tempRightPivot = tempRightStart + midPoint(len(tempRightArray))
    tempRightRightEnd = tempRightStart+  len(tempRightArray)-1
    quickSort(arr, tempRightPivot, tempRightStart, tempRightRightEnd)
    

ArrayElems = [61, 173, 180, 227, 220, 441, 448, 467, 48, 70, 85, 103, 114, 141, 148, 161, 173, 180, 227, 269, 311, 371, 405, 417]
quickSort(ArrayElems,midPoint(len(ArrayElems)), 0, len(ArrayElems)-1)
print(ArrayElems)