import random

#Define chance and community chest cards
chance = {
    0: 'Advance to "Go". (Collect $200)',
    1: 'Advance to Illinois Ave. If you pass Go, collect $200.',
    2: 'Advance to St. Charles Place. If you pass Go, collect $200.',
    3: 'Advance token to the nearest Utility. If unowned, you may buy it from the Bank. If owned, throw dice and pay owner a total 10 (ten) times the amount thrown.',
    4: 'Advance to the nearest Railroad. If unowned, you may buy it from the Bank. If owned, pay owner twice the rent to which they are otherwise entitled. If Railroad is unowned, you may buy it from the Bank. (First card, there are 2 of these)',
    5: 'Advance to the nearest Railroad. If unowned, you may buy it from the Bank. If owned, pay owner twice the rent to which they are otherwise entitled. If Railroad is unowned, you may buy it from the Bank. (Second card, there are 2 of these)',
    6: 'Bank pays you dividend of $50.',
    7: 'Get out of Jail Free. This card may be kept until needed, or traded/sold.',
    8: 'Go Back Three Spaces.',
    9: 'Go to Jail. Go directly to Jail. Do not pass GO, do not collect $200.',
    10: 'Make general repairs on all your property: For each house pay $25, For each hotel pays $100.',
    11: 'Take a trip to Reading Railroad. Advance token to Reading Railroad. If you pass Go, collect $200.',
    12: 'Pay Poor Tax of $15.',
    13: 'Take a walk on the Boardwalk. Advance token to Boardwalk.',
    14: 'You have been elected Chairman of the Board. Pay each player $50.',
    15: 'Your building loan matures. Receive $150.'
}
community_chest = {
    0: 'Advance to "Go". (Collect $200)',
    1: 'Bank error in your favor. Collect $200.',
    2: 'Doctors fees. Pay $50.',
    3: 'From sale of stock you get $50.',
    4: 'Get Out of Jail Free. This card may be kept until needed or sold/traded.',
    5: 'Go to Jail. Go directly to jail. Do not pass Go, Do not collect $200.',
    6: 'Grand Opera Night. Collect $50 from every player for opening night seats.',
    7: 'Holiday Fund matures. Receive $100.',
    8: 'Income tax refund. Collect $20.',
    9: 'It is your birthday. Collect $10 from every player.',
    10: 'Life insurance matures. Collect $100',
    11: 'Hospital Fees. Pay $50.',
    12: 'School fees. Pay $50.',
    13: 'Receive $25 consultancy fee.',
    14: 'You are assessed for street repairs: Pay $40 per house and $115 per hotel you own.',
    15: 'You have won second prize in a beauty contest. Collect $10.',
    16: 'You inherit $100.'
}
# Define the properties and their positions
properties = {
    0: 'Go',
    1: 'Mediterranean Avenue',
    2: 'Community Chest',
    3: 'Baltic Avenue',
    4: 'Income Tax',
    5: 'Reading Railroad',
    6: 'Oriental Avenue',
    7: 'Chance',
    8: 'Vermont Avenue',
    9: 'Connecticut Avenue',
    10: 'Jail/Just Visiting',
    11: 'St. Charles Place',
    12: 'Electric Company',
    13: 'States Avenue',
    14: 'Virginia Avenue',
    15: 'Pennsylvania Railroad',
    16: 'St. James Place',
    17: 'Community Chest',
    18: 'Tennessee Avenue',
    19: 'New York Avenue',
    20: 'Free Parking',
    21: 'Kentucky Avenue',
    22: 'Chance',
    23: 'Indiana Avenue',
    24: 'Illinois Avenue',
    25: 'B&O Railroad',
    26: 'Atlantic Avenue',
    27: 'Ventnor Avenue',
    28: 'Water Works',
    29: 'Marvin Gardens',
    30: 'Go To Jail',
    31: 'Pacific Avenue',
    32: 'North Carolina Avenue',
    33: 'Community Chest',
    34: 'Pennsylvania Avenue',
    35: 'Short Line',
    36: 'Chance',
    37: 'Park Place',
    38: 'Luxury Tax',
    39: 'Boardwalk'
}

# Define the colors of the properties
colors = {
    'brown': [1, 3],
    'light blue': [6, 8, 9],
    'pink': [11, 13, 14],
    'orange': [16, 18, 19],
    'red': [21, 23, 24],
    'yellow': [26, 27, 29],
    'green': [31, 32, 34],
    'dark blue': [37, 39]
}

# Define the prices of the properties
prices = {
    1: 60,
    3: 60,
    5: 200,
    6: 100,
    8: 100,
    9: 120,
    11: 140,
    12: 150,
    13: 140,
    14: 160,
    15: 200,
    16: 180,
    18: 180,
    19: 200,
    21: 220,
    23: 220,
    24: 240,
    25: 200,
    26: 260,
    27: 260,
    28: 150,
    29: 280,
    31: 300,
    32: 300,
    34: 320,
    35: 200,
    37: 350,
    39: 400
}

# Define the player's starting money
money = 1500

# Define the player's position
position = 0

# Define a function to roll the dice
def roll_dice():
    return random.randint(1, 6) + random.randint(1, 6)

# Define a function to check if a property is owned
def is_owned(property):
    return property in owned_properties

# Define a function to buy a property
def buy_property(property):
    global money
    if money >= prices[property]:
        money -= prices[property]
        owned_properties.append(property)
        print(f"You bought {properties[property]} for ${prices[property]}")
    else:
        print("You don't have enough money to buy this property")

# Define a function to pay rent on a property
def pay_rent(property):
    rent = prices[property] // 10
    owner = property_owners[property]
    owner_money = player_money[owner]
    if owner_money >= rent:
        player_money[owner] -= rent
        money += rent
        print(f"You paid ${rent} in rent to {player_names[owner]}")
    else:
        print(f"{player_names[owner]} doesn't have enough money to collect rent")

# Define a function to handle landing on a property
def handle_property(property):
    if is_owned(property):
        if property_owners[property] == player:
            print("You already own this property")
        else:
            pay_rent(property)
    else:
        buy_property(property)

# Define the players
num_players = int(input("How many players? "))
player_names = []
player_money = []
owned_properties = []
property_owners = {}
for i in range(num_players):
    name = input(f"Enter player {i+1}'s name: ")
    player_names.append(name)
    player_money.append(money)

# Play the game
while True:
    player = position % num_players
    print(f"{player_names[player]}'s turn")
    input("Press enter to roll the dice")
    move = roll_dice()
    position += move
    print(f"You rolled {move} and landed on {properties[position]}")
    if position in [2, 17, 33]:
        print("Community Chest")
    elif position in [7, 22, 36]:
        print("Chance")
    elif position == 30:
        print("Go to Jail")
        position = 10
    elif position == 4:
        print("Income Tax")
        player_money[player] -= 200
    elif position == 38:
        print("Luxury Tax")
        player_money[player] -= 75
    elif position == 20:
        print("Free Parking")
    elif position == 10:
        print("Jail/Just Visiting")
    elif position in colors['brown']:
        handle_property(position)
    elif position in colors['light blue']:
        handle_property(position)
    elif position in colors['pink']:
        handle_property(position)
    elif position in colors['orange']:
        handle_property(position)
    elif position in colors['red']:
        handle_property(position)
    elif position in colors['yellow']:
        handle_property(position)
    elif position in colors['green']:
        handle_property(position)
    elif position in colors['dark blue']:
        handle_property(position)
    elif position in [5, 15, 25, 35]:
        print("Railroad")
    elif position in [12, 28]:
        print("Utility")
    else:
        print("Error: Invalid position")
    print(f"{player_names[player]} has ${player_money[player]}")
    if input("Continue playing? (y/n) ").lower() == 'n':
        break
