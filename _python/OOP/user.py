#Create bank account class
class BankAccount:
    def __init__(self, starting_int_rate = 0.01, starting_balance = 0):
        self.balance = starting_balance
        self.int_rate = starting_int_rate

    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
            return self

        self.balance -= amount
        return self
    
    # def display_account_info(self):
    #     print(f"Balance: {self.balance}")
    #     return self

    def yeild_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
            return self

        return self



#Create a new class class User
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = {"savings": BankAccount(0.005),
                        "current": BankAccount(0.02)}

    #adds the deposited amount into the account balance
    def make_depoist(self, account_name, amount):
        self.account[account_name].deposit(amount)
        print(f"{self.name} Deposited {amount}$ to {account_name} account\n")
        return self

    #Withdraws money from the account balance
    def make_withdrawal(self, account_name, amount):
        self.account[account_name].withdraw(amount)
        print(f"{self.name} Withdrew {amount}$ from {account_name} account\n")
        return self

    #display user's name and current balance
    def display_user_balance(self, account_name):
        print(f"Username: {self.name} Balacnce: ${self.account[account_name].balance} in {account_name} account\n")
        return self

#create new instances of the class User
michael = User("Michael", "mich@example.com")
anna = User("Anna", "anna@example.com")
monty = User("Monty","monty@example.com")

#First user
michael.make_depoist("savings",100).make_depoist("current",200).make_depoist("current",212).make_withdrawal("current",250).display_user_balance("current").display_user_balance("savings")

#Second User
# anna.make_depoist(300).make_depoist(2100).make_withdrawal(32).make_withdrawal(1000).display_user_balance()

#Thrid User
# monty.make_depoist(20).make_withdrawal(15).make_withdrawal(2.5).make_withdrawal(2).display_user_balance()
