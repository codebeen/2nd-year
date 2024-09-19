from array import *

arr = array('i', [20, 30, 89, 1, 67, 44, 78])
first = second = third = 0 #initialize to zero

for i in range(0, len(arr)):
    if arr[i] > first:
        third = second
        second = first
        first = arr[i]
    elif arr[i] > second:
        third = second
        second = arr[i]
    else:
        third = arr[i]

print("First largest number: ", first)
print("Second largest number: ", second)
print("Third largest number: ", third)