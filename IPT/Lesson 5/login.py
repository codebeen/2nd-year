def login(users):
    """Function to handle user login"""
    while True:
        username = input("Enter your username: ")
        if username in users:
            while True:
                password = input("Enter your password: ")
                if password == users[username]:
                    print("Login successful! Welcome, {}!".format(username))
                    return
                else:
                    print("Invalid password.")
        else:
            print("Invalid username.")

def main():
    # Dictionary containing usernames and passwords
    users = {
        'migo': 'raine24',
        'darben': 'shanella',
        'heart': 'nikcole',
        'klei': 'ishia',
        'gerard': 'queen',
        'bernardo': 'password6',
        'lamonte': 'password7',
        'delapaz': 'password8',
        'pagatpatan': 'password9',
        'cuadra': 'password10'
    }

    # Attempt login
    login(users)

if __name__ == "__main__":
    main()
