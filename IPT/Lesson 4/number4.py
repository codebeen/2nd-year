# Write a program that asks the user to enter size of list and input a list of integers. Do the following:list = []while True:    list_length = input("Enter the length of the list: ")        try:        list_length = int(list_length)                # ask user to input numbers to store in the list        for i in range(0, list_length):            while True:                element = input("Enter a number: ")                                try:                    list.append(int(element))                    break                except ValueError:                    print("Invalid input! Must be integer")        break    except ValueError:        print("Invalid input! Must be integer")        print("\nYour list: ")       print(list)# calculate the sumsum = 0for item in list:    sum += itemprint("\nA: The sum of elements in the list: ", sum)# Print the last item in the list.print("B: The last item in the list: ", list[-1])# Print the list in reverse order.print("C: List in reverse order: ", end="")list.reverse()print(list)#Print Yes if the list contains a 5 and No otherwisefor item in list:    if item == 5:        contain_five = True        break    else:        contain_five = False        if contain_five == True:    print("D: Yes")else:    print("D: No")        # Print how many integers in the list are less than 5counter = 0for item in list:    if item < 5:        counter += 1 print("E: Number of integers in the list that is less than 5: ", counter)# Remove the first and last items from the list, sort the remaining items,and print the result.list.pop(0)list.pop(-1)list.sort()print("F: Removed the first and last element")print(list)