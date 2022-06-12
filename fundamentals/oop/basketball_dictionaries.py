# Assignment Basketball Dictionaries

"""
Challenge 1: Update the Constrictor
Update the constrictor to accept a dictionary with a single player's 
info instead of individual arguments for attribuites
"""
class Player:
    def __init__(self, player):
        self.name = player['name']
        self.age = player['age']
        self.position = player['position']
        self.team = player['team']

# __repr__ is used to format class to terminal
    def __repr__(self):
        display = f"player: {self.name}, age: {self.age}, position: {self.position}, team: {self.team}" 
        return display


thomas = {
    'name': 'Thomas Muller', 
    'age': 32, 
    'position': 'Attacking midfielder', 
    'team': 'Bayern Munchen'
}

jonas = {
    'name': 'Jonas Hofmann',
    'age': 29,
    'position': 'Attacking midfielder',
    'team': 'Borussia M\'Gladbach'
}

lukas = {
    'name': 'Lukas Klostermann',
    'age': 26,
    'position': 'Center back',
    'team': 'RB Leipzig'
}

timo = {
    'name': 'Timo Werner',
    'age': 26,
    'position': 'Striker',
    'team': 'Chelsea'
}


"""
Challenge 2: Create instances using individual player dictionaries
NOTE: I had all ready created data before realizing I was suppose to 
use the provided data. I just left it because it is the same basic
thing... hopefully that is ok.
"""

player_thomas = Player(thomas)
print(player_thomas)

player_jonas = Player(jonas)
print(player_jonas)

player_lukas = Player(lukas)
print(player_lukas)

player_timo = Player(timo)
print(player_timo)

"""
Challenge 3: Make a list of Player instances for a list of dictionaries
Populate a new list with Player instances from the list of players
"""

players_lst = [
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

# Solution for challenge 3

new_list = []

for item in range(len(players_lst)):
    temp_name = f"player_{players_lst[item]['name']}"
    temp_name = temp_name.lower()
    temp_name = temp_name.replace(' ', '_')

    temp_name = Player(players_lst[item])
    new_list.append(temp_name)
    # print(temp_name.name)

for item in new_list:
    print(item)
