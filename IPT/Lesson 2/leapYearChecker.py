# a program that checks if the year is a leap year

year = eval(input("Enter the year: "))

if year % 4 == 0 or (year % 100 and year % 400):
    print("The year is a Leap year")
else:
    print("The year is not a Leap year")