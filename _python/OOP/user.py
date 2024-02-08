#Create a new class class User
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

#create new instances of the class User
michael = User("Michael", "mich@example.com")
anna = User("Anna", "anna@example.com")

print(michael.name)
