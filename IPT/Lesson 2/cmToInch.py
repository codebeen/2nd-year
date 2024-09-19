# a program that converts centimeters to inch

while True:
    # ask the user to input the length in cm
    cm = eval(input("Enter the length in cm: "))

    if cm > 0:
        inch = cm / 2.54
        print(f"{cm} cm is equal to {inch:.2f} in")
        break
    else:
        print("Invalid input. Must not be less than zero")