def Merge(arr2, l, mid, h):
    n1 = mid-l+1
    n2 = h-mid

    A = [0]*n1
    B = [0]*n2


    for i in range(0, n1):
        A[i] = arr2[l+i]
    
    for j in range(0, n2):
        B[j] = arr2[mid+1+j]

    i = 0
    j = 0
    k = l
    

    while i < n1 and j < n2:
        if A[i] <= B[j]:
            arr2[k] = A[i]
            i += 1
        else:
            arr2[k] = B[j]
            j += 1
        k += 1

    while i < n1:
        arr2[k] = A[i]
        i += 1
        k += 1

    while j < n2:
        arr2[k] = B[j]
        j += 1
        k += 1


def MergeSort(arr1, l,h):
    if l < h:
        mid = l+(h-l)//2
        MergeSort(arr1, l, mid)
        MergeSort(arr1, mid+1, h)
        Merge(arr1, l, mid, h)



arr1 = [2, 8, 15, 18, 5, 9, 12, 17, 21, 22, 23, 25]
print("Array before sorting is", arr1)
l = 0
h = len(arr1)

MergeSort(arr1, l , h-1)
print("Array after sorting is", arr1)
