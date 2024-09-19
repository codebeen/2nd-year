# Write a program that will ask user to input a list of integer tuples. Ask also for another integer value and assign it to K. Output the tuple that are divisible by k
  
def value_for_k():
    while True:
        k = input("Enter value for k: ")
            
        try:
            k = int(k)
           
           #calls function that are divisible by k
            print(f"\nDivisible by {k}: ", divisible_by_k(tuples, k))
            break # exits the loop
           
        except(ValueError):
            print("Invalid input! Must be an integer")
          
          
def divisible_by_k(num_list, k):
    divisible = ()
    
    for num in num_list:
        if num % k == 0:
            divisible += (num, )
     
    #returns the tuples that is divisible by k
    return divisible
    
    
# starts the program
tuples = ()

while True:
    user_input = input("Enter a number (q to terminate): ").lower()
            
    if user_input == "q":
        break
    elif user_input.isdigit():  # check if the number is integer
        user_input = int(user_input)
        tuples += (user_input,) # add item to tuples
    else:
        print("Invalid input! Must be an integer")
            
# calls the function to input value for k
value_for_k()