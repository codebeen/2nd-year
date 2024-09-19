from array import *

arr = array('i', [23, 0, 0, 7, 2, 0, 15, 45, 0, 32, 0, 57])

#print the original values inside the array
print("Given Array: ")
for i in arr:
    print(i, end=" ")

for i in range(0, len(arr)):
    if arr[i] == 0: #checks if equal to zero
        arr.append(arr[i]) #add to the end of the array
        arr.remove(arr[i]) #remove the value to avoid duplication

#print the new values inside an array
print("\n\nNew values: ")
for i in arr:
    print(i, end=" ")