"""
Starting with the list of the previous exercise, write Python statements to do the following:
"""

# Previous List
my_list = [67, 62.9, 'hi', False, 8, 67, 'apple', 6.5]

print('Previous List:', my_list)
print('\n')


# a. Append “banana” and 67 to the list.
my_list.append("banana")
my_list.append(67)
print('A:', my_list)

# b. Insert the value “dog” at position 3.
my_list.insert(3, "dog")
print('B:', my_list)

# c. Insert the value 909 at the start of the list.
my_list.insert(0, 909)
print('C:', my_list)

# d. Find the index of “hi”.
hi_index = my_list.index("hi")
print('D: The Index of "hi":', hi_index)

# e. Count the number of 67s in the list.
num_67 = my_list.count(67)
print("E: Number of occurrences of 67:", num_67)

# f. Remove the first occurrence of 67 from the list.
my_list.remove(67)
print('F:', my_list)

# g. Remove False from the list using pop and index.
my_list.pop(4)
print('G:', my_list)