def binary_search(arr, x):
    low = 0
    mid = 0
    high = len(arr)-1

    while low <= high:
        mid = (low+high)//2
        if arr[mid] < x:
            low  = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

arr = [1,2,3,9,11,13,17,25,57,90]
x = 61
result = binary_search(arr, x)
if result != -1:
    print("Number is present at position:", result)
else:
    print("Number is not present in an array")
