"""
Create a list with the following six items: 67, 62.9, “hi”, False, 8, 67, ‘apple’, 6.5.
Begin with the empty list shown below, and add 8 statements to add each item, one per item.
The first four statements should use the append method to append the item to the list,
and the last four statements should use concatenation
"""

list = []

#add items using append
list.append(67)
list.append(62.9)
list.append("hi")
list.append(False)

# prints created list using append
print("List created using append: ")
print(list)

#add items using concatenation
list = list + [8]
list = list + [67]
list = list + ["apple"]
list = list + [6.5]

# prints list created using concatenation
print("\nList created  using concatenation: ")
print(list)