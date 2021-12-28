class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, name):
        if len(name) >= 2 and len(name)<= 10:
            self.name = name
        else:
            print("Please enter a valid username length.")

    def change_pin(self, pin):
        if len(str(pin)) == 4:
            self.pin = pin
        else:
            print("Please enter a PIN with only 4 numbers.")

    def change_password(self, password):
        if len(password) >= 5:
            self.password = password
        else:
            print("Please enter a valid password length.")

class BankUser(User):

    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0

    def show_balance(self):
        print(self.name, "has an account balance of:", "${:.2f}".format(self.balance))

    def withdraw(self, amount):
        self.amount = amount
        self.balance -= self.amount

    def deposit(self, amount):
        self.amount = amount
        self.balance += self.amount

    def transfer_money(self, _user, amount):
        while True:
            if amount < 0:
                print("Only positive numbers can be deposited!")
                exit()
            else:
                break
        print("You are transferring", "${:.2f}".format(amount), "to", _user.name)
        print("Authentication required")
        transfer_auth = int(input("Enter your PIN: "))
        if transfer_auth == self.pin:
            self.balance -= amount
            _user.balance += amount
            print("Transfer authorized")
            print("Transferring", "${:.2f}".format(amount), "to", _user.name)
            return True
        else:
            print("Invalid PIN. Transaction cancelled")
            return False

    def request_money(self, _user, amount):
        print("You are requesting", "${:.2f}".format(amount), "from", _user.name)
        print("User authentication is required...")
        request_pin = int(input("Enter PIN: "))
        # Check if entered PIN matches user's PIN
        if request_pin != _user.pin:
            print("Invalid PIN. Transaction canceled.")
            return False
        request_pass = input("Enter your password: ").lower()
        # Check if entered password matches user's password
        if request_pass != self.password:
            print("Invalid password. Transaction canceled.")
            return False
        # Adds amount to balance of user requesting and removes amount from other user.
        if request_pin == _user.pin and request_pass == self.password:
            self.balance += amount
            _user.balance -= amount
            print("Request authorized")
            print(_user.name, "sent", "${:.2f}".format(amount))
            return True
        else:
            print("Invalid credentials. Transaction cancelled")


bankuser1 = BankUser("Bob", 1234, "password")
bankuser2 = BankUser("Alice", 5678, "alicepassword")
bankuser2.deposit(5000)
bankuser2.show_balance()
bankuser1.show_balance()
print()

transferred = bankuser2.transfer_money(bankuser1, 500)
bankuser2.show_balance()
bankuser1.show_balance()
print()

if transferred:
    bankuser2.request_money(bankuser1, 250)
    bankuser2.show_balance()
    bankuser1.show_balance()

''' Output:
        Alice has an account balance of: 5000
        Bob has an account balance of: 0     

        You are transferring $500 to Bob
        Authentication required
        Enter your PIN: 5678
        Transfer authorized
        Transferring $500 to Bob
        Alice has an account balance of: 4500
        Bob has an account balance of: 500   

        You are requesting $250 from Bob     
        User authentication is required...
        Enter Bob's PIN: 1234
        Enter your password: alicepassword
        Request authorized
        Bob sent $250
        Alice has an account balance of: 4750
        Bob has an account balance of: 250
'''
