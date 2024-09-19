# Write a program that asks the user for an integer and creates a list that consists of the factors of that integer

def factors(number):
    factors = []
    
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    
    return factors
    
    
while True:
    number = input("Enter an integer: ")
    
    try:
        number = int(number)
        factor_list = factors(number)
        print("The list of factors: ", factor_list)
        break
    except ValueError:
        print("Invalid input! Must be an integer")