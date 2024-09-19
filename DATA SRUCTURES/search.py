from array import *

# get the size of the array
def element():
    num_elem = int(input("Enter number of elements: "))

    if num_elem < 3:
        print("Error! Must be minimum of 3\n")
        return element()
    elif num_elem > 5:
        print("Error! Must be maximum of 5\n")
        return element()
    else:
        return num_elem


# input values into the array
def input_value(array, size):
    for i in range(size):
        value = int(input("Enter a number: "))
        array.append(value)
    
    return array


# sort the array using bubble sort
def bubble_sort(array, size):
    for i in range(size):
        for j in range(0, size - i - 1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    
    return array


# search the number entered using binary search
def search(array, low, high):
    result = None
    num = int(input("\nEnter a number to be searched: "))
    
    while high >= low:
        mid = (high + low) // 2
        
        if num == array[mid]:
            result = 0
            print("Sorted array: ")
            display(arr)
            print("\nThe element", num, "is found")
            break
        elif num > array[mid]:
            low = mid + 1
        else:
            high = mid - 1
        
    if result is None:
        print("Element ", num, "is not found")
        return search(array, 0, len(array) - 1)


def display(array):
    for x in array:
        print(x, end = " ")


arr = array('i', [ ])

size = element()
arr = input_value(arr, size)
arr = bubble_sort(arr, size)
search(arr, 0, size - 1)