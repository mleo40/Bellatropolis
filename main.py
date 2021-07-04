# Bellatropolis
# v0.0.2
# bella/mike

# A D&D like game, with a Dungeon master and any number of players

# we need a dictionary to store player designs in
player_design = {}

# base race characteristics
race_strength = {'elf': 10, 'ork': 20, 'wizard': 7, 'human': 8}
race_health = {'elf': 20, 'ork': 10, 'wizard': 30, 'human': 15}
race_speed = {'elf': 30, 'ork': 5, 'wizard': 30, 'human': 15}

# Print backstory:
print("Welcome to Bellatropolis!   A village not on any map.  A village with a dark secret.  "
      "It is your task, should you choose it, to unravel the mystery that haunts this village\n")


def dmaster() -> dict:
    """
      This function will create a dungeon master
      :return: dict of character traits
      """
    print("Dungeon Masters can only be Elves or Wizards")

    dmaster_design = {'name': input('Dungeon Masters Name: ').lower(),
                      'age': input('Age of the Dungeon Master: ').lower(),
                      'height': input('Height of the Dungeon Master: ').lower(),
                      'race': input('Elf or Wizard? ').lower()
                      }

    return dmaster_design


def make_player(player_name: str) -> dict:
    """
      this function will create players
      :return: dict of character traits
      """
    player_design[player_name] = {'age': int(input(f'Age of Player {player_name} ').lower()),
                                  'height': int(input(f'Height of Player {player_name} ').lower()),
                                  'race': input(f'Race of Player (Elf/Ork/Wizard/Human) {player_name} ').lower(),
                                  }
    player_design[player_name]['strength'] = race_strength[player_design[player_name]['race']]
    player_design[player_name]['health'] = race_health[player_design[player_name]['race']]
    player_design[player_name]['speed'] = race_health[player_design[player_name]['race']]

    return player_design


def town(player_design):
    """
    This will manage actions in the town
    :return:
    """
    print(player_design)
    print('Entering town, you are met with stares from all the crazy people who live here.\n'
          'You hear them whisper to each other and themselves.\n'
          'You catch words like "get out now, while you can", and other ominous speech.\n')

    print(next(iter(player_design)) + ' has a bad feeling about this.')


def forest():
    """
    This will manage actions in the forest
    :return:
    """
    pass


def hills():
    """
    This will manage actions in the hills
    :return:
    """
    pass


# build a dictionary describing the dungeon master:
dungeon_master_design = dmaster()

# get number of players and their names:
num_players = int(input('Enter the number of victims: '))
player_names = []
for n in range(num_players):
    player_names.append(input('players name: '))

# build each character and add them all to the same dictionary for reference later:
for player in player_names:
    make_player(player)

print("You stand at the crossroads.\n"
      "Ominous music plays...\n"
      "In front of you, the road leads to the only town for miles.\n"
      "To the left, the forest\n"
      "The right, the hills.\n"
      "There is no going back.\n"
      "Choo"
      "print(player_design)se.\n"
      )

direction = input("Town/Forest/Hills: ").capitalize()
if direction == "Town":
    town(player_design)
elif direction == "Hills":
    hills(player_design):
elif direction == "Forest":
    forest(player_design)
else:
    print("You were eaten by goblins for your bad reading, typing or spelling skills")
