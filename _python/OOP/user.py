#Create a new class class User
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_depoist(self, amount):
        self.account_balance += amount

#create new instances of the class User
michael = User("Michael", "mich@example.com")
anna = User("Anna", "anna@example.com")

print(f"Username: {michael.name} Balance: {michael.account_balance}$")
michael.make_depoist(100)
print("Deposited 100$")
print(f"Username: {michael.name} Balance: {michael.account_balance}$")
michael.make_depoist(200)
print("Deposited 200$")
print(f"Username: {michael.name} Balance: {michael.account_balance}$")
