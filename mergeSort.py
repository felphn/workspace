def mergeSort(arr):
    if len(arr) > 1:
        leftArr = arr[:len(arr)//2]
        rightArr = arr[len(arr)//2:]
        mergeSort(leftArr)
        mergeSort(rightArr)
        a = b = c = 0
        while a < len(leftArr) and b < len(rightArr):
            if leftArr[a] < rightArr[b]:
                arr[c] = leftArr[a]
                a+=1
            else:
                arr[c] = rightArr[b]
                b+=1
            c+=1
        while a < len(leftArr):
            arr[c] = leftArr[a]
            a+=1
            c+=1
        while b < len(rightArr):
            arr[c] = rightArr[b]
            b+=1
            c+=1


valueLst = [15, 2, 7, 26, 35, 9, 4, 8, 52, 68]
print(f'List: {valueLst}')
mergeSort(valueLst)
print(f'Sorted List: {valueLst}')