# a program that prints message based on the temperature

temperature = eval(input("Enter the temperature in Celsius: "))

if temperature < -273.15:
    print("Temperature is invalid because it is below absolute zero")
elif temperature == -273.15:
    print("Temperature is absolute zero")
elif temperature > -273.15 and temperature < 0:
    print("Temperature is below freezing")
elif temperature == 0:
    print("Temperature is at freezing point")
elif temperature < 100 and temperature > 0:
    print("Temperature is in the normal range")
elif temperature == 100:
    print("Temperature is at the boiling point")
elif temperature > 100:
    print("Temperature is above the boiling point")
else: 
    print("Invalid input")
