#Create a new class class User
class User:
    def __init__(self):
        self.name = "Baraa"
        self.email = "example@example.com"
        self.account_balance = 0

#create new instances of the class User
michael = User()
anna = User()

print(michael.name)

#setting michael name
michael.name = "Michael"
print(michael.name)