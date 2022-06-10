# Users with BankAccounts

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

    def withdraw(self, amount):
        """
        Decrease the account balance by the given amount if there are 
        sufficient funds, if there is not enough money, charge a 
        insufficient_funds_fee
        """
        # Minimun balance for credit union saving acct is $5
        if amount > self.balance - 5:
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
        print("BANK ACCOUNT INFO:")
        print(f"Account type: {self.type_of_acct}")
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
        self.account = {
            'saving': BankAccount(balance=0, type_of_acct='saving', int_rate=2),
            'checking': BankAccount(balance=0, type_of_acct='checking', int_rate=4)
        }

    def display_info(self):
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
            return 1
        elif choice == 'checking':
            return 2
        else:
            print("You must enter 'saving' or 'checking' to make a deposit. Try again")
            self.choose_bank_account()

    def make_deposit(self):
        """Make deposit into users BankAccount"""
        print("MAKE A DEPOSIT:")
        amount = int(input("Enter in the amount to deposit: $"))
        acct_type = self.choose_bank_account()
        if acct_type == 1:
            self.account['saving'].deposit(amount)
        else:
            self.account['checking'].deposit(amount)

    def make_withdraw(self):
        """Make withdraw from users BankAccount"""
        print("MAKE A WITHDRAW:")
        amount = int(input("Enter in the amount to deposit: $"))
        acct_type = self.choose_bank_account()
        if acct_type == 1:
            self.account['saving'].withdraw(amount)
        else:
            self.account['checking'].withdraw(amount)

    def display_user_balance(self):
        """Display user account balance from BankAccount"""
        print(f"DISPLAY ACCOUNT BALANCE:")
        acct_type = self.choose_bank_account()
        if acct_type == 1:
            self.account['saving'].display_account_info()
        else:
            self.account['checking'].display_account_info()

# Create user
user_neal = Users('neal', 'cassady', 'cowboy@bus.com', 53)

"""
Used chaining methods to display user info, enroll in rewards club,
and display bank account info
"""
user_neal.display_info().enroll()
# Make a deposit to users account
user_neal.make_deposit()
user_neal.make_deposit()

# Make a withdraw from users account
user_neal.make_withdraw()

user_neal.display_user_balance()

# Run the classmethod
# BankAccount.print_accounts()
