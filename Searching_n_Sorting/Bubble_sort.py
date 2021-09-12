arr = [25, 17, 31, 13, 2]
print("Array before sorting is:", arr)
for i in range(len(arr)):
    for j in range(len(arr)-1):
        if arr[j] > arr[j+1]:
            arr[j+1], arr[j] = arr[j], arr[j+1]


print("Array after sorting is:", arr)

