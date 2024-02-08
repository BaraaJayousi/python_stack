#Create a new class class User
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    #adds the deposited amount into the account balance
    def make_depoist(self, amount):
        self.account_balance += amount
        print(f"{self.name} Deposited {amount}$\n")
    
    #Withdraws money from the account balance
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        print(f"{self.name} Withdrawn {amount}$\n")

    #display user's name and current balance
    def display_user_balance(self):
        print(f"Username: {self.name} Balance: {self.account_balance}$\n")

    #Trnsfer amount of money from current user to a specified user of type User
    def make_transfer(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_depoist(amount)
        print(f"Money transfer of {amount}$. From {self.name} To {other_user.name}\n")


#create new instances of the class User
michael = User("Michael", "mich@example.com")
anna = User("Anna", "anna@example.com")
monty = User("Monty","monty@example.com")

#First user
michael.make_depoist(100)
michael.make_depoist(200)
michael.make_depoist(212)
michael.make_withdrawal(250)

#Second User
anna.make_depoist(300)
anna.make_depoist(2100)
anna.make_withdrawal(32)
anna.make_withdrawal(1000)
anna.display_user_balance()



#Thrid User
monty.make_depoist(20)
monty.make_withdrawal(15)
monty.make_withdrawal(2.5)
monty.make_withdrawal(2)
monty.display_user_balance()

#Trnasfer between first and third users
michael.make_transfer(monty,100)
michael.display_user_balance()
monty.display_user_balance()