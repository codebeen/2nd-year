# Define the variables x and y as lists of numbers
x = [1, 2, 3, 4, 5]
y = [11, 12, 13, 14, 15]
z = (21, 22, 23, 24, 25)

# a. What is the value of 3*x?
print('A:', 3*x)

# b. What is the value of x+y?
print('B:', x+y)

# c. What is the value of x-y?
print("C: TypeError: unsupported operand type")

# d. What is the value of x[1]?
print('D:', x[1])

# e. What is the value of x[0]?
print('E:', x[0])

# f. What is the value of x[-1]?
print('F:', x[-1])

# g. What is the value of x[:]?
print('G:', x[:],)

# h. What is the value of x[2:4]?
print('H:', x[2:4])

# i. What is the value of x[1:4:2]?
print('I:', x[1:4:2])

# j. What is the value of x[:2]?
print('J:', x[:2])

# k. What is the value of x[::2]?
print('K:', x[::2])

# l. What is the result of the following two expressions?
x[3] = 8
print('L:', x)
