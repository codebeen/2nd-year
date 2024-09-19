"""""
Start with the list [8,9,10]. Do the following: 
"""

start_list = [8,9,10]
print('Starting List:', start_list)

# a. Set the second entry (index 1) to 17 
start_list[1] = 17
print("\nA: ", start_list)

# b. Add 4, 5, and 6 to the end of the list 
start_list.extend([4,5,6])
print("B: ", start_list)

# c. Remove the first entry from the list 
start_list.pop(0)
print("C: ", start_list)

# d. Sort the list 
start_list.sort()
print("D: Sorted List: ", start_list)

# e. Double the list 
start_list = start_list * 2
print("E: ", start_list)

# f. Insert 25 at index 3 
start_list.insert(3, 25)
print("F: ", start_list)

# The final list should equal [4,5,6,25,10,17,4,5,6,10,17] 
print("\nFinal list: ", start_list)