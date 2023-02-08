import json
import os


class Bank:
    def __init__(self):
        self.isLoggedIn = False  # later we will use this to check if user is logged in or not
        self.minWithdraw = 500
        self.maxWithdraw = 15000
        self.userIndex = 0  # index of user in users.json
        self.users = []  # list of users

        if (os.path.exists("users.json")):  # check if users.json file exists
            with open("users.json", "r") as users:
                self.users = json.load(users)
        else:  # if users.json file does not exist then create it
            with open("users.json", "w") as users:
                json.dump(self.users, users)

    def createAc(self):
        print("----Create Account----")
        username = ''
        isUserExist = True
        while (isUserExist):  # check if username already exist
            username = input("Enter username : ")
            for user in self.users:
                if (user['username'] == username):
                    os.system("cls")
                    print("Username already exist\nPlease try again\n")
                    break
            else:
                isUserExist = False

        # if username does not exist then create account
        password = input("Enter password : ")
        balance = int(input("Enter initial balance : "))

        # add user to users.json
        self.users.append({
            "username": username,
            "password": password,
            "balance": balance
        })
        with open("users.json", "w") as users:
            json.dump(self.users, users)
        os.system("cls")
        print("Account created successfully\n")

    def login(self):
        print("----Login----")
        isValid = False
        while (not isValid):  # check if username and password is valid
            username = input("Enter username : ")
            password = input("Enter password : ")
            for user in self.users:
                if (user['username'] == username and user['password'] == password):
                    self.username = username
                    self.password = password
                    self.balance = user['balance']
                    self.isLoggedIn = True
                    self.userIndex = self.users.index(user)
                    isValid = True
                    break
            else:
                os.system("cls")
                print("Invalid username or password\nPlease try again\n")

    def logout(self):
        # reset all variables
        self.username = ''
        self.password = ''
        self.isLoggedIn = False
        print(f"{self.username} you are logged out.\n")

    def withdraw(self):
        amount = int(input("Enter amount : "))
        if (amount >= self.minWithdraw and amount <= self.maxWithdraw):  # check if amount is valid
            if (amount <= self.balance):  # check if amount is less than available balance
                self.balance -= amount
                print(f"Amount {amount} withdrawn successfully")
                print(f"Available balance is {self.balance}\n")
                self.users[self.userIndex]['balance'] = self.balance

                # update users.json
                with open("users.json", "w") as users:
                    json.dump(self.users, users)
            else:
                print("Insufficient balance\n")
        else:
            print("Invalid amount")

    def deposit(self):
        amount = int(input("Enter amount : "))
        self.balance += amount  # add amount to available balance
        print(f"Amount {amount} deposited successfully")
        print(f"Available balance is {self.balance}\n")
        self.users[self.userIndex]['balance'] = self.balance

        # update users.json
        with open("users.json", "w") as users:
            json.dump(self.users, users)

    def checkBalance(self):
        # print account details
        print(f"Account username is {self.username}")
        print(f"Available balance is {self.balance}\n")


def menu():
    print("1. Create Account")
    print("2. Login")
    print("0. Exit")


def loginMenu():
    print("1. Withdraw")
    print("2. Deposit")
    print("3. Check Balance")
    print("4. Logout")


choice = 1
bank = Bank()
while (choice != 0):
    # check if user is logged in or not
    if (bank.isLoggedIn):
        loginMenu()
    else:
        menu()

    choice = int(input("Enter your choice : "))

    if (bank.isLoggedIn):
        if (choice == 1):
            os.system("cls")
            bank.withdraw()
        elif (choice == 2):
            os.system("cls")
            bank.deposit()
        elif (choice == 3):
            os.system("cls")
            bank.checkBalance()
        elif (choice == 4):
            os.system("cls")
            bank.logout()
    else:
        if (choice == 1):
            os.system("cls")
            bank.createAc()
            subChoice = int(input("Do you want to login? (1/0) : "))
            if (subChoice == 1):
                os.system("cls")
                bank.login()

        elif (choice == 2):
            os.system("cls")
            bank.login()
            if (bank.isLoggedIn):
                os.system("cls")
                print("Login successful\n")

        elif (choice == 0):
            os.system("cls")
            print("Thank you for using our service\n")
        else:
            os.system("cls")
            print("Invalid choice\n")
