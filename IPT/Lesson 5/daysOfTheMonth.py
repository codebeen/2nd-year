# Dictionary of days in the months of the year
days = {'January': 31, 'February': 28, 'March': 31, 'April': 30, 'May': 31, 'June': 30,
        'July': 31, 'August': 31, 'September': 30, 'October': 31, 'November': 30, 'December': 31}

def get_days_in_month():
    """Function to get the number of days in a month"""
    while True:
         month_name = input("Enter a month name: ").capitalize()
         
         if month_name in days:
             print("Number of days in", month_name, ":", days[month_name])
             break
         else:
            print("Input month is not in the list")

def print_sorted_keys():
    """Function to print all keys in alphabetical order"""
    sorted_keys = sorted(days.keys())
    print("Months in alphabetical order:")
    for month in sorted_keys:
        print(month)

def print_months_with_31_days():
    """Function to print months with 31 days"""
    print("Months with 31 days:")
    for month, days_count in days.items():
        if days_count == 31:
            print(month)

def print_sorted_pairs():
    """Function to print (key-value) pairs sorted by number of days"""
    sorted_pairs = sorted(days.items(), key=lambda x: x[1])
    print("Months sorted by number of days:")
    for month, days_count in sorted_pairs:
        print(month, ":", days_count)

def main():
    # Part a: Ask user for month name
    get_days_in_month()

    # Part b: Print keys in alphabetical order
    print()
    print_sorted_keys()
    print()

    # Part c: Print months with 31 days
    print_months_with_31_days()
    print()

    # Part d: Print (key-value) pairs sorted by number of days
    print_sorted_pairs()
    print()

if __name__ == "__main__":
    main()

