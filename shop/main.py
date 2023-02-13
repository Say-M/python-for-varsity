import os
import json


class Shop:
    def __init__(self):
        self.products = []  # list of products
        self.cart = []  # list of products in cart
        self.users = []  # list of users
        self.checkout = []  # list of products in checkout
        self.user = {
            "id": 0,
            "username": "",
            "password": "",
            "role": ""
        }  # current user
        if (os.path.exists("products.json")):  # check if products.json file exists
            with open("products.json", "r") as products:
                self.products = json.load(products)
        else:  # if products.json file does not exist then create it
            with open("products.json", "w") as products:
                json.dump(self.products, products)

        if (os.path.exists("users.json")):  # check if users.json file exists
            with open("users.json", "r") as users:
                self.users = json.load(users)
        else:  # if users.json file does not exist then create it
            with open("users.json", "w") as users:
                json.dump(self.users, users)

        if (os.path.exists("checkout.json")):  # check if checkout.json file exists
            with open("checkout.json", "r") as checkout:
                self.checkout = json.load(checkout)
        else:  # if checkout.json file does not exist then create it
            with open("checkout.json", "w") as checkout:
                json.dump(self.checkout, checkout)

    def createAccount(self):
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
        role = int(input("Enter role (1 for admin, 2 for customer) : "))

        # add user to users.json
        self.users.append({
            "id": len(self.users) + 1,
            "username": username,
            "password": password,
            "role": "admin" if role == 1 else "customer"
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
                    self.user = user
                    isValid = True
                    break
            else:
                os.system("cls")
                print("Invalid username or password\nPlease try again\n")

    def logout(self):
        # reset all variables
        print(f"{self.user['username']} you are logged out.\n")
        self.user = {
            "id": 0,
            "username": "",
            "password": "",
            "role": ""
        }
        self.cart = []

    def addProduct(self):
        print("----Add Product----")
        name = input("Enter product name : ")
        price = int(input("Enter product price : "))
        quantity = int(input("Enter product quantity : "))
        self.products.append({
            "id": len(self.products) + 1,
            "name": name,
            "price": price,
            "quantity": quantity
        })
        with open("products.json", "w") as products:
            json.dump(self.products, products)
        os.system("cls")
        print("Product added successfully\n")

    def removeProduct(self):
        print("----Remove Product----")
        self.showProducts()
        productId = int(input("Enter product id : "))
        for product in self.products:
            if (product['id'] == productId):
                self.products.remove(product)
                print("Product removed successfully\n")

                # update products.json
                with open("products.json", "w") as products:
                    json.dump(self.products, products)
                break
        else:
            print("Product not found\n")

    def updateProduct(self):
        print("----Update Product----")
        self.showProducts()
        productId = int(input("Enter product id : "))
        for product in self.products:
            if (product['id'] == productId):
                name = input("Enter product name : ")
                price = int(input("Enter product price : "))
                quantity = int(input("Enter product quantity : "))
                product['name'] = name
                product['price'] = price
                product['quantity'] = quantity
                print("Product updated successfully\n")

                # update products.json
                with open("products.json", "w") as products:
                    json.dump(self.products, products)
                break
        else:
            print("Product not found\n")

    def showProducts(self):
        print("----Products----")
        for product in self.products:
            print(f"ID : {product['id']}")
            print(f"Name : {product['name']}")
            print(f"Price : {product['price']}")
            print(f"Quantity : {product['quantity']}")
            print("-------------")

    def addToCart(self):
        print("----Add to Cart----")
        self.showProducts()
        productId = int(input("Enter product id : "))
        quantity = int(input("Enter quantity : "))
        for product in self.products:
            if (product['id'] == productId):
                if (product['quantity'] >= quantity):
                    self.cart.append({
                        "id": product['id'],
                        "name": product['name'],
                        "price": product['price'],
                        "quantity": quantity,
                        "total": product['price'] * quantity,
                        "userId": self.user['id']
                    })
                    product['quantity'] -= quantity
                    print("Product added to cart successfully\n")

                    # update products.json
                    with open("products.json", "w") as products:
                        json.dump(self.products, products)
                else:
                    print("Not enough quantity\n")
                break
        else:
            print("Product not found\n")

    def showCart(self):
        print("----Cart----")
        for product in self.cart:
            print(f"ID : {product['id']}")
            print(f"Name : {product['name']}")
            print(f"Price : {product['price']}")
            print(f"Quantity : {product['quantity']}")
            print("-------------")

    def removeFromCart(self):
        print("----Remove from Cart----")
        self.showCart()
        productId = int(input("Enter product id : "))
        for product in self.cart:
            if (product['id'] == productId):
                self.cart.remove(product)
                print("Product removed from cart successfully\n")

                # update products.json
                for p in self.products:
                    if (p['id'] == productId):
                        p['quantity'] += product['quantity']
                        with open("products.json", "w") as products:
                            json.dump(self.products, products)
                        break
                break
        else:
            print("Product not found\n")

    def purchase(self):
        print("----Purchase----")
        if (len(self.cart) == 0):
            print("Cart is empty\n")
            return

        isPurchase = input("Are you sure you want to purchase? (y/n) : ")
        if (isPurchase == 'y'):
            self.showCart()
            self.checkout = self.cart
            self.cart = []
            with open("checkout.json", "w+") as checkout:
                json.dump(self.checkout, checkout)
                self.checkout = json.load(checkout)
            print("Purchase successfully\n")
        else:
            print("Purchase canceled\n")

    def showPurchases(self):
        print("----Purchases----")
        for product in self.checkout:
            if (product['userId'] == self.user['id']):
                print(f"ID : {product['id']}")
                print(f"Name : {product['name']}")
                print(f"Price : {product['price']}")
                print(f"Quantity : {product['quantity']}")
                print("-------------")


def menu():
    print("----Menu----")
    print("1. Create Account")
    print("2. Login")
    print("0. Exit")


def adminMenu():
    print("----Menu----")
    print("1. Add Product")
    print("2. Update Product")
    print("3. Show Products")
    print("4. Remove Product")
    print("5. Logout")


def customerMenu():
    print("----Menu----")
    print("1. Add to Cart")
    print("2. Show Cart")
    print("3. Remove from Cart")
    print("4. Checkout")
    print("5. Show Purchases")
    print("6. Logout")


choice = 1
shop = Shop()
while (choice):
    if (shop.user['username']):
        if (shop.user['role'] == 'admin'):
            adminMenu()
        else:
            customerMenu()
    else:
        menu()

    choice = int(input("Enter your choice : "))
    if (shop.user['username']):
        if (shop.user['role'] == 'admin'):
            if (choice == 1):
                os.system("cls")
                shop.addProduct()
            elif (choice == 2):
                os.system("cls")
                shop.updateProduct()
            elif (choice == 3):
                os.system("cls")
                shop.showProducts()
            elif (choice == 4):
                os.system("cls")
                shop.removeProduct()
            elif (choice == 5):
                os.system("cls")
                shop.logout()
            else:
                print("Invalid choice\n")
        elif (shop.user['role'] == 'customer'):
            if (choice == 1):
                os.system("cls")
                shop.addToCart()
            elif (choice == 2):
                os.system("cls")
                shop.showCart()
            elif (choice == 3):
                os.system("cls")
                shop.removeFromCart()
            elif (choice == 4):
                os.system("cls")
                shop.purchase()
            elif (choice == 5):
                os.system("cls")
                shop.showPurchases()
            elif (choice == 6):
                shop.logout()
            else:
                print("Invalid choice\n")
    else:
        if (choice == 1):
            os.system("cls")
            shop.createAccount()
            subChoice = int(input("Do you want to login? (1/0) : "))
            if (subChoice):
                os.system("cls")
                shop.login()

        elif (choice == 2):
            os.system("cls")
            shop.login()
        elif (choice == 0):
            os.system("cls")
            print("Thank you for using our service\n")
            break
        else:
            print("Invalid choice\n")
