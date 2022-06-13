# Assignment Basketball Dictionaries

"""
Challenge 1: Update the Constrictor
Update the constrictor to accept a dictionary with a single player's 
info instead of individual arguments for attribuites
"""

class Player:
    """Create a model of a player"""

    def __init__(self, player):
        self.name = player['name']
        self.age = player['age']
        self.position = player['position']
        self.team = player['team']

    def __repr__(self):
        """__repr__ is used to format class print to terminal"""
        display = f"player: {self.name}, age: {self.age}, position: {self.position}, team: {self.team}" 
        return display

    """
    Creat a classmethod for taking a list of dictonaries and creating
    a list of instances
    """
    @classmethod
    def add_player(cls, players_lst):
        """Add player to all_players list for class"""
        all_players = []
        for player in players_lst:
            all_players.append(cls(player))
        return all_players

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
print()

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

"""
Solution for challenge 3
Take a list of dictionaries and produce a new list of instances
"""

new_list = []

for item in range(len(players_lst)):
    temp_name = f"player_{players_lst[item]['name']}"
    temp_name = temp_name.lower()
    temp_name = temp_name.replace(' ', '_')

    temp_name = Player(players_lst[item])
    new_list.append(temp_name)
    # print(temp_name.name)

# Print out instances in new_list
for item in new_list:
    print(item)
print()
# NINJA BONUS: add a get_team(cls, team_list) and @classmethod
all_players = Player.add_player(players_lst)

for player in all_players:
    print(player)

