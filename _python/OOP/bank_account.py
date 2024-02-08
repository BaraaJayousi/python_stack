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
    
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yeild_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
            return self

        return self


#Testing the class
savings_account = BankAccount(0.02)
current_account = BankAccount(0.021, 2000)

savings_account.display_account_info().deposit(3000).display_account_info().yeild_interest().display_account_info().withdraw(100).display_account_info()
current_account.display_account_info().deposit(3000).display_account_info().yeild_interest().display_account_info().withdraw(100).display_account_info()