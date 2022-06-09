# Coding Dojo Assignment: BankAccount: using classes
# Import math class for rounding yield interest
import math

class BankAccount:
    """Model a standard sav account"""

    def __init__(self, balance=5, type_of_acct='sav', int_rate=4):
        """
        Model a savings acct w/ default interest rate (%)
        and starting balance: min for sav is $5
        """
        self.balance = balance
        self.type_of_acct = type_of_acct
        self.int_rate = int_rate
        self.num_withdraws = 0
        self.num_deposits = 0

    def deposit(self, amount):
        """Increase the account balance by the given amount"""
        print("DEPOSIT")
        print(f"Deposit amount: {amount}")
        self.balance += amount
        print(f"New account balance: {self.balance}\n")
        self.num_deposits += 1
        return self

    def insufficient_funds_fee(self):
        """
        When insufficient funds: withdraw $5 from account and 
        print a message: 'insufficient funds: charging a $5 fee
        """
        self.balance -= 5
        print(f"Insufficient funds: charging a $5 fee\n") 
        return self

    def withdraw(self, amount):
        """
        Decrease the account balance by the given amount if there are 
        sufficient funds, if there is not enough money, charge a 
        insufficient_funds_fee
        """
        # Minimun amount for sav acct is 5
        if amount > self.balance - 5:
            self.insufficient_funds_fee()
            print(f"New balnce: {self.balance}\n")
        else:
            print("WITHDRAW")
            print(f"Account balance: {self.balance}")
            self.balance -= amount
            print(f"Withdraw amount: {amount}")
            print(f"New balance: {self.balance}\n")
        self.num_withdraws += 1
        return self

    def display_account_info(self, acct_num):
        """Print to console: eg. 'banlance: $100'"""
        print(f"Account Information for {acct_num}:")
        print(f"Account balance: {self.balance}")
        print(f"Account interest rate: {self.int_rate}")
        print(f"Number of deposits: {self.num_deposits}")
        print(f"Number of withdraws: {self.num_withdraws}\n")
        return self

    def yield_interest(self):
        """
        Increase the account balance by the current balance * the
        interest rate as long as the balance is positive amt
        """
        if self.balance > 0:
            # Use math to round for ease of assignment
            print(f"Calculating interest yield for the month:")
            amt = int(math.ceil(self.balance * (self.int_rate / 100)))
            self.balance += amt
            print(f"Account earned ${amt} this month")
            print(f"New balance: {self.balance}\n")
        return self


# Test the class

# First account and starting balance of 100; use default int_rate
print()
acct_001 = BankAccount(100, 'sav')
acct_001.display_account_info('acct_001')

"""
First Acct: use chainging to: make 3 deposits and 1 withdrawl, yield interest,
and display account info
"""
acct_001.deposit(100).deposit(1000).withdraw(750).deposit(250).yield_interest().display_account_info('acct_001')

# Second acct with start balance 500 and interest rate: 7%
acct_002 = BankAccount(500, 'chk', 7)
acct_002.display_account_info('acct_002')

"""
Second Acct: use chaining to: make 2 deposits and 4 withdraws, yield interest,
and display acct info.
"""
acct_002.deposit(2500).withdraw(1000).withdraw(500).deposit(2000).withdraw(3000).yield_interest().display_account_info('acct_002')

"""
Bonus: use a classmethod to print all instances of a BankAccount's info
"""

