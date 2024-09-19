# a program that convert celsius to farenheit and vice versa

temperature = eval(input("Enter the temperature to be converted: "))

while True:
    unit = input("Enter the unit of the temperature (Celsius or Farenheit): ").lower()

    if unit == "celsius":
        farenheit = ((9/5) * temperature) + 32
        print(f"{temperature} celsius is equal to {farenheit:.2f} farenheit")
        break
    elif unit == "farenheit":
        celsius =  ((5/9) * temperature) - 32
        print(f"{temperature} farenheit is equal to {celsius:.2f} celsius")
        break
    else:
        print("Invalid input. Please enter celsius or farenheit")