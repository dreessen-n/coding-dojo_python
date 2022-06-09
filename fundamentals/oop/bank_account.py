# Coding Dojo Assignment: BankAccount: using classes
# Import math class for rounding yield interest
import math

class BankAccount:

    """Model a standard credit union bank account"""
    all_accounts = []

    def __init__(self, name='acct_XXX', balance=5, type_of_acct='sav', int_rate=4):
        """
        Model a savings acct w/ default interest rate (%)
        and starting balance: min for sav is $5
        """
        self.name = name
        self.balance = balance
        self.type_of_acct = type_of_acct
        self.int_rate = int_rate
        self.num_withdraws = 0
        self.num_deposits = 0
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        """Increase the account balance by the given amount"""
        print(f"DEPOSIT for: {self.name}")
        print(f"Deposit amount: ${amount}")
        self.balance += amount
        print(f"New account balance: ${self.balance}\n")
        self.num_deposits += 1
        return self

# Created extra method to calculate fee
    def insufficient_funds_fee(self, withdraw_amt):
        """
        When insufficient funds: withdraw $5 from account and 
        print a message: 'insufficient funds: charging a $5 fee
        """
        self.balance -= 5
        print(f"WITHDRAW for {self.name}")
        print(f"Account balance: ${self.balance}. Withdraw request: ${withdraw_amt}")
        print(f"Insufficient funds for {self.name}: charging a $5 fee") 
        return self

    def withdraw(self, amount):
        """
        Decrease the account balance by the given amount if there are 
        sufficient funds, if there is not enough money, charge a 
        insufficient_funds_fee
        """
        # Minimun balance for credit union sav acct is $5
        if amount > self.balance - 5:
            self.insufficient_funds_fee(amount)
            print(f"New balnce: ${self.balance}\n")
        else:
            print(f"WITHDRAW for {self.name}")
            print(f"Account balance: ${self.balance}")
            self.balance -= amount
            print(f"Withdraw amount: ${amount}")
            print(f"New balance: ${self.balance}\n")
        self.num_withdraws += 1
        return self

    def display_account_info(self):
        """Print to console: eg. balance: $100"""
        print("ACCOUNT INFO:")
        print(f"Account name: {self.name}")
        print(f"Account balance: ${self.balance}")
        print(f"Account interest rate: {self.int_rate}%")
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
            print(f"Calculating interest yield (monthly) for {self.name}:")
            print(f"Account balance: ${self.balance}")
            print(f"Interest rate: {self.int_rate}%")
            amt = int(math.ceil(self.balance * (self.int_rate / 100)))
            self.balance += amt
            print(f"Account earned ${amt}")
            print(f"New balance: ${self.balance}\n")
        return self

# Add a classmethod for printing all instances
    @classmethod
    def print_accounts(cls):
        for acct in cls.all_accounts:
            print(f"Account name: {acct.name}")
            print(f"Account balance: ${acct.balance}")
            print(f"Account type: {acct.type_of_acct}")
            print(f"Account interest rate: {acct.int_rate}%")
            print(f"Account number of deposits: {acct.num_deposits}")
            print(f"Account number of withdrawls: {acct.num_withdraws}\n")

# First account and starting balance of 100; use default int_rate
print()
acct_001 = BankAccount('acct_001', 100, 'sav')
print(f"ACCOUNT CREATED:")
acct_001.display_account_info()

"""
First Acct: use chainging to: make 3 deposits and 1 withdrawl, yield interest,
and display account info
"""
acct_001.deposit(100).deposit(1000).withdraw(750).deposit(250).yield_interest().display_account_info()

# Second acct with start balance 500 and interest rate: 7%
acct_002 = BankAccount('acct_002', 500, 'chk', 7)
print(f"ACCOUNT CREATED:")
acct_002.display_account_info()

"""
Second Acct: use chaining to: make 2 deposits and 4 withdraws, yield interest,
and display acct info.
"""
acct_002.deposit(2500).withdraw(1000).withdraw(500).deposit(2000).withdraw(3000).yield_interest().withdraw(550).display_account_info()

"""
Bonus: use a classmethod to print all instances of a BankAccount's info
"""
BankAccount.print_accounts()
