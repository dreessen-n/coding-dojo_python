# Python OOP - user assignment

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

    def display_info(self):
        """Display user info"""
        full_name = f"{self.first_name} {self.last_name}"
        print(f"\nUser information:\n")
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


    def enroll(self):
        """Enroll user into rewards member and add 200 points"""
        if self.is_rewards_member == False:
            print(f"Welcome to Rewards, {self.first_name}!")
            self.is_rewards_member = True
            self.gold_card_points += 200
            print(f"{self.first_name} you now have {self.gold_card_points} points")
        else:
            print(f"{self.first_name} you are already a rewards member")

    def spend_points(self, amount):
        """Redeem reward points if member has them"""
        if self.gold_card_points > amount:
            self.gold_card_points -= amount
            print(f"\n{self.first_name} you have redeemed {amount} points")
        else:
            print(f"\n{self.first_name} you do not have enough points to redeem")



# Create user
user_neal = Users('neal', 'dreessen', 'dreessen.edu@gmail.com', 53)

# Displya user info
user_neal.display_info()

# Enroll user into rewards
print(f"Join rewards club\n")
user_neal.enroll()

# Display user info again to show enrollment
user_neal.display_info()

# Redeem points
print(f"Redeem Rewards Points:")
user_neal.spend_points(50)

# Display ueer info again to show new balance on points
user_neal.display_info()

# Check to see if enrolled in rewwards
user_neal.enroll()

# Try to redeem more points than you have
user_neal.spend_points(400)
