def add_products(dictionary):
    # Function to add products and prices to the dictionary
    while True:
        product_name = input("Enter product name (or 'done' to finish): ")
        
        if product_name.lower() == 'done':
            break
        
        # ask user for price
        while True:  
            price = input("Enter price for {}: ".format(product_name))
            
            #checks if input is numeric
            try:
                if float(price) > 0:
                    dictionary[product_name] = float(price)
                    break
                else:
                    print("Must be greater than zero")
            except ValueError:
                print("Invalid input! Must be a numeric value")

def find_price(dictionary):
    # Function to find and print price of a product
    while True:
        product_name = input("Enter product name to find its price (or 'done' to finish): ")
        if product_name.lower() == 'done':
            break
        elif product_name in dictionary:
            print("Price of {} is: {}".format(product_name, dictionary[product_name]))
        else:
            print("Product not found.")

def main():
    products = {}
    add_products(products)
    find_price(products)

if __name__ == "__main__":
    main()
