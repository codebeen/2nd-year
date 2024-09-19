# Write a Python program to create a list of tuples having first element as the number and second element as the square of the number. Input: list = [1, 2, 3] Output: [(1, 1), (2, 4), (3, 9)]


def squares_list(input_list):
    output_list = [] #initialize empty list to hold the list of tuples
     
    for num in input_list:
        output_list.append((num, num ** 2))
     
    # return the output list
    return output_list
    
   
# initialize the input list
input_list = [1, 2, 3]
#print the input_list
print("Input: ", input_list)

# output_list will hold the return value of squares_list()
output_list = squares_list(input_list)
#prints the output_list
print("Output: ", output_list)