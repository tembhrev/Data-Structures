"""
The number of comparisions in case of sorted list might be less as compared
to unsorted list because the search need not always continue till the end of
the list
"""

arr = [11, 2, 9, 13, 57, 25, 17, 1, 90, 3]
num = int(input("Enter number  to be searched:"))
pos = 0
for i in range(len(arr)):
    if num == arr[i]:
        pos = i
        break

if pos == 0:
    print("Number is not present in an array")
else:
    print("Number is present at memory:", pos)
    
    
