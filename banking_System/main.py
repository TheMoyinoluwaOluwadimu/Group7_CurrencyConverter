import random

database_one = {
    'Folu': 'olu',
    'Fola': 'ola',
    'moyin': 'moyin'
}
'to store user info from registration'
users = {}


def login():
    # login function here
    name = input("Enter your name? \n")
    password = input("Enter your password? \n")
    if name in database_one and password == database_one[name]:
        print("Welcome " + name)
        return True
    else:
        print("Password or Username Incorrect. Please try again")
        return False


def generate_account_number():
    account_number = ''
    for i in range(10):
        account_number += str(random.randint(0, 9))
    return account_number


def register():
    name = input("Please Enter your name: ")
    password = input("Enter your password: ")

    # Generate a random account number
    account_number = generate_account_number()
    while account_number in database_one:
        account_number = generate_account_number()

        users[account_number] = {
            'name': name,
            'password': password,
            'balance': 0.0
        }

    print("Registration successful! Your account number is: ", account_number + ("\n"))


def bankOperations():
    print('What do you want to do today:')
    print('1. Withdrawal')
    print('2. Cash Deposit')
    print('3. Complaint')
    print('4. Logout')

    selectedOption = int(input('Please select an option:'))

    if selectedOption == 1:
        print('you want a %s' % selectedOption)
        bankOperations()

    elif selectedOption == 2:
        print('you want to do a %s' % selectedOption)
        bankOperations()

    elif selectedOption == 3:
        print('you have %s' % selectedOption)
        bankOperations()

    elif selectedOption == 4:
        exit()
    else:
        print('Invalid Option selected, please try again')


print("Welcome, what would you like to do?")
print("1. Login")
print("2. Register")

actionSelect: int = int(input("Select an option \n"))

if (actionSelect == 2):
    register()
    print(" \n")
    print("Welcome, what would you like to do?")
    print("1. Login")
    print("2. Register")

    actionSelect: int = int(input("Select an option \n"))

    # print("Log into your account\n")
    # login()

if (actionSelect == 1):
    isLoginSuccessful = False

    while isLoginSuccessful == False:
        isLoginSuccessful = login()

    bankOperations()

else:
    print('Login failed, username or password incorrect')

if __name__ == '__main__':
    actionSelect()
