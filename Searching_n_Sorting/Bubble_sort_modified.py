arr = [13, 2, 17, 25, 31]
n = 0
for i in range(len(arr)):
    swap = False
    for j in range(len(arr)-1):
        if arr[j] > arr[j+1]:
            arr[j+1], arr[j] = arr[j], arr[j+1]
            swap = True
        


        if swap == False:
            break

        
        

print("Array before sorting is:", arr)
print("Array after sorting is:", arr)
print(n)
