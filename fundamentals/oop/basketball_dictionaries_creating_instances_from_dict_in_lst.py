# Assignment Basketball Dictionaries

"""
Challenge 1: Update the Constrictor
Update the constrictor to accept a dictionary with a single player's 
info instead of individual arguments for attribuites
"""
class Player:
    def __init__(self, players):
        self.name = players['name']
        self.age = players['age']
        self.position = players['position']
        self.team = players['team']


players = [
    {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
    },
    {
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
    },
    {
    "name": "Kyrie Irving", 
    "age":32, 
    "position": "Point Guard", 
    "team": "Brooklyn Nets"
    },
    {
    "name": "Damian Lillard", 
    "age":33, 
    "position": "Point Guard", 
    "team": "Portland Trailblazers"
    },
    {
    "name": "Joel Embiid", 
    "age":32, 
    "position": "Power Foward", 
    "team": "Philidelphia 76ers"
    },
    {
    "name": "", 
    "age":16, 
    "position": "P", 
    "team": "en"
    }
]

"""
Challenge 2: Create instances using individual player dictionaries
Pull dictionary of players from list and create instances of player
"""


"""
Challenge 3: Make a list of Player instances for a list of dictionaries
"""

for item in range(len(players)):
    temp_name = f"player_{players[item]['name']}"
    temp_name = temp_name.lower()
    temp_name = temp_name.replace(' ', '_')

    temp_name = Player(players[item])
    print(temp_name.name)


