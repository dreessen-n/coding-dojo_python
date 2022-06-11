# Users with BankAccounts
# Import math class for rounding yield interest
import math

class BankAccount:

    """Model a standard credit union bank account"""
    all_accounts = []

    def __init__(self, balance=5, type_of_acct='saving', int_rate=4):
        """
        Model a savings acct w/ default interest rate (%)
        and starting balance: min for saving is $5
        """
        self.balance = balance
        self.type_of_acct = type_of_acct
        self.int_rate = int_rate
        self.num_withdraws = 0
        self.num_deposits = 0
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        """Increase the account balance by the given amount"""
        print(f"DEPOSIT:")
        print(f"Deposit amount: ${amount}")
        self.balance += amount
        print(f"New balance: ${self.balance}\n")
        self.num_deposits += 1
        return self

# Created extra method to calculate fee
    def insufficient_funds_fee(self, withdraw_amt):
        """
        When insufficient funds: withdraw $5 from account and 
        print a message: insufficient funds: charging a $5 fee
        """
        self.balance -= 5
        print(f"WITHDRAW:")
        print(f"Account balance: ${self.balance}. Withdraw request: ${withdraw_amt}")
        print(f"Insufficient funds: charging a $5 fee\n") 
        return self


    def balance_check(self, withdraw_amt):
        """Check to see if enough funds before attempting to transfer"""
        if withdraw_amt > self.balance:
            print("Not sufficient funds; transaction cancelled")
            return False
        else:
            print("Sufficient funds to transfer")
            return True

    def withdraw(self, amount):
        """
        Decrease the account balance by the given amount if there are 
        sufficient funds, if there is not enough money, charge a 
        insufficient_funds_fee
        """
        if amount > self.balance:
            self.insufficient_funds_fee(amount)
            print(f"New balance: ${self.balance}\n")
        else:
            print(f"WITHDRAW:")
            print(f"Account balance: ${self.balance}")
            self.balance -= amount
            print(f"Withdraw amount: ${amount}")
            print(f"New balance: ${self.balance}\n")
        self.num_withdraws += 1
        return self

    def display_account_info(self):
        """Print to console: eg. balance: $100"""
        print("==============================================")
        print("BANK ACCOUNT INFO/BALANCE:")
        print(f"Account type: {self.type_of_acct}")
        print(f"Account balance: ${self.balance}")
        print(f"Account interest rate: {self.int_rate}%")
        print(f"Number of deposits: {self.num_deposits}")
        print(f"Number of withdraws: {self.num_withdraws}")
        print("==============================================\n")
        return self

    def yield_interest(self):
        """
        Increase the account balance by the current balance * the
        interest rate as long as the balance is positive amt
        """
        if self.balance > 0:
            # Use math to round for ease of assignment
            print(f"Calculating interest yield (monthly):")
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
            acct.display_account_info()

class Users:
    """Create a model of a user"""

    def __init__(self, first_name, last_name, email, age):
        """Initialize the attributes for the user"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
        self.account = [
            {'saving': BankAccount(balance=0, type_of_acct='saving', int_rate=2)},
            {'checking': BankAccount(balance=0, type_of_acct='checking', int_rate=4)}
        ]

    def display_open_acct_info(self):
        """Display user info"""
        full_name = f"{self.first_name} {self.last_name}"
        print(f"\nUser information:")
        print(f"User: {full_name}")
        print(f"User email: {self.email}")
        print(f"User age: {self.age}")
        if self.is_rewards_member == True:
            print(f"{self.first_name} is a rewards member")
        else:
            print(f"{self.first_name} is not a rewards members")
        if self.gold_card_points == 0:
            print(f"{self.first_name} has no gold card points\n")
        else:
            print(f"{self.first_name} has {self.gold_card_points} points\n")
        return self

    def enroll(self):
        """Enroll user into rewards member and add 200 points"""
        if self.is_rewards_member == False:
            print(f"Welcome to Rewards, {self.first_name}!")
            self.is_rewards_member = True
            self.gold_card_points += 200
            print(f"{self.first_name} you now have {self.gold_card_points} points\n")
        else:
            print(f"{self.first_name} you are already a rewards member\n")
        return self

    def spend_points(self, amount):
        """Redeem reward points if member has them"""
        if self.gold_card_points > amount:
            self.gold_card_points -= amount
            print(f"{self.first_name} you have redeemed {amount} points")
        else:
            print(f"{self.first_name} you do not have enough points to redeem")
            print(f"you only have {self.gold_card_points} points")
        return self

    def choose_bank_account(self):
        """Choose which BankAccount to access"""
        choice = input("Choose account, enter: 'saving' or 'checking': ")
        if choice == 'saving':
            return 0
        elif choice == 'checking':
            return 1
        else:
            print("You must enter 'saving' or 'checking' to make a deposit. Try again")
            self.choose_bank_account()

    def make_deposit(self, amount, acct_type_deposit=1):
        """Make deposit into users BankAccount"""
        if acct_type_deposit == 0:
            self.account[0]['saving'].deposit(amount)
        else:
            self.account[1]['checking'].deposit(amount)

    def make_withdraw(self, amount, acct_type_withdraw=1):
        """Make withdraw from users BankAccount"""
        if acct_type_withdraw == 0:
            self.account[0]['saving'].withdraw(amount)
        else:
            self.account[1]['checking'].withdraw(amount)

    def display_user_balance(self):
        """Display user account balance from BankAccount"""
        print(f"DISPLAY ACCOUNT BALANCES:")
        self.account[0]['saving'].display_account_info()
        self.account[1]['checking'].display_account_info()

    def transfer_money(self, transfer_user):
        """Transfer money to another user"""

        print("TRANSFER MONEY TO ANOTHER USER:")

        # Get transfer money amount:
        amount = int(input("Amount to transfer: $"))

        # Select account to transfer money from
        print("TRANSFER FROM:")
        acct_type_from = self.choose_bank_account()
        if acct_type_from == 1:
            # Check for enought money to transfer
            enough_money = self.account['saving'].balance_check(amount)
            if enough_money:
                self.account['saving'].withdraw(amount)
            else:
                print("Insufficient funds; transaction cancelled")
                return
        elif acct_type_from == 2:
            # Check for enought money to transfer
            enough_money = self.account['checking'].balance_check(amount)
            if enough_money:
                self.account['checking'].withdraw(amount)
            else:
                print("Insufficient funds; transaction cancelled")
                return

        # Transfer to the other account
        transfer_user.account['checking'].balance += amount

        print("TRANSFTER COMPLETE:\n")
        print("FROM ACCOUNT...\n")
        user_neal.display_user_balance()
        print("TO ACCOUNT...\n")
        transfer_user.display_user_balance()

# Create user
user_neal = Users('neal', 'cassady', 'cowboy@bus.com', 53)

# Display users opening account info and enroll in rewards
user_neal.display_open_acct_info().enroll()

# Make deposit user_neal account:
amount_deposit = int(input("Amount to deposit: $"))
acct_type_deposit = user_neal.choose_bank_account()
user_neal.make_deposit(amount_deposit, acct_type_deposit)

# Make another deposit user_neal account:
amount_deposit = int(input("Amount to deposit: $"))
acct_type_deposit = user_neal.choose_bank_account()
user_neal.make_deposit(amount_deposit, acct_type_deposit)

# Make a withdraw from users account
amount_withdraw = int(input("Amount to withdraw: $"))
acct_type_withdraw = user_neal.choose_bank_account()
user_neal.make_withdraw(amount_withdraw, acct_type_withdraw)

# Display account balance and other info
user_neal.display_user_balance()

# Create a second user for SENPAI BONUS
user_dude = Users('Jeff', 'lebowski', 'send_money@cash.com', 85)

# Display user_dude opening account info and enroll in rewards
user_dude.display_open_acct_info().enroll()

# Display other user opening account info
# Make deposit user_dude account:
amount_deposit = int(input("Amount to deposit: $"))
acct_type_deposit = user_dude.choose_bank_account()
user_dude.make_deposit(amount_deposit, acct_type_deposit)

# Display account balance and other info
user_dude.display_user_balance()

# Run the classmethod
# BankAccount.print_accounts()

# Trasfer money to from user_neal to user_transfer
# user_neal.transfer_money(user_dude)
