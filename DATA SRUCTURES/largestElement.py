from array import *

arr = array('i', [ ])
num = None
largest = 0

def elements():
    num_elements = int(input("Enter number of elements: "))
    
    if num_elements < 5:
        print("Error! Must be minimum of 5\n")
        return elements()
    elif num_elements > 10:
        print("Error! Must be maximum of 10\n")
        return elements()
    else:
        return num_elements

length = elements()
for x in range(length):
    num = int(input("Enter a number: "))
    arr.append(num)

for i in range(length):
    if arr[i] > largest:
        largest = arr[i]

print("Largest Element: ", largest)