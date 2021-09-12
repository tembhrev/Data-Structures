def partition(l, h):

    pivot = A[l]
    i = l
    j = h

    while i < j:

        while A[i] <= pivot:
            i += 1

        while A[j] > pivot:
            j -= 1

        if i < j:
            A[i], A[j] = A[j], A[i]

    A[l], A[j] = A[j], A[l]

    return j

def QuickSort(l, h):
    if l < h:
        j = partition(l, h)
        QuickSort(l, j)
        QuickSort(j+1, h)



A = [10, 16, 8, 12, 15, 6, 3, 9, 5]
l = 0
h = len(A)-1
print("Array before sorting:")
print(A)

QuickSort(l, h)

print("Array After sorting:")
print(A)
