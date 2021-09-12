arr = [25, 17, 31, 13, 2]

for i in range(len(arr)-1):
    for j in range(i+1,len(arr)):
        if arr[i] > arr[j]:
            arr[j], arr[i] = arr[i], arr[j]

print("Array before sorting is:", arr)
print("Array after sorting is:", arr)
