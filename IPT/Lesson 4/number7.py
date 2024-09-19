# Write a program that removes any repeated items from a list so that each item appears at most once.


list = [1,1,2,3,4,3,0,0]
print('The original list is :', list)

# Removing the repeated items
unique = []
for item in list:
    if item not in unique:
        unique.append(item)
        
print('The list after removing the repeated items:', unique)