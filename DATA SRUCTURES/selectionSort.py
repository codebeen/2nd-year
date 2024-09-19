from array import *

def select_sort(array):
    for i in range(len(arr)):
        min_index = i

        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

arr = array('i', [6, 8, 67, 1, 78, 2, 9, 4, 22, 18, 30])

print("Unsorted array: ")
for x in arr:
    print(x, end = " ")

select_sort(arr)
print("\n\nSorted array: ")
for x in arr:
    print(x, end = " ")