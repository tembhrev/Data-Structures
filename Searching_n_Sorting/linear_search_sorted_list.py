arr = [1,2,3,9,11,13,17,25,57,90]
num = int(input("Enter number to be searched:"))

for i in range(len(arr)):
    if arr[len(arr)-1] < num or arr[i] >= num:
        if arr[i] == num:
            print("Number is present at position:", i)
        else:
            print("Number is not present in an array")
        break

    
