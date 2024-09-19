# a program that ask  how many credits a student have taken

credits = eval(input("Enter the number of credits you have taken: "))

if credits < 23 and credits > 0:
    print("You are a freshman")
elif credits >= 24 and credits <= 53:
    print("You are a sophomore")
elif credits >= 54 and credits <= 83:
    print("You are a junior")
elif credits >= 84:
    print("You are a senior")
else:
    print("Invalid input.")