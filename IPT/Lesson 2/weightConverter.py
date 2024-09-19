# a program that converts kilogram to pounds

while True:
    weight = eval(input("Enter the weight in kilogram (kg): "))

    if weight >= 0:
        weight_lb = weight * 2.2046
        print(f"{weight} kg is equal to {weight_lb:.2f} lb")
        break
    else:
        print("Invalid input. Please enter a number greater than 0")