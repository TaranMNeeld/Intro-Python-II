from room import Room
from player import Player
from item import Item
from prettier import Prettier

# Declare all the rooms

item = {
    'torch': Item('torch',
                  'the flame glows bright'),
    'dagger': Item('dagger',
                   'it seems dull...'),
    'shield': Item('shield',
                   'sturdy enough to block an arrow')
}

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     [item['torch']]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
                    passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
                    into the darkness. Ahead to the north, a light flickers in
                    the distance, but there is no way across the chasm.""",
                     [item['dagger']]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
                    to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
                    chamber! Sadly, it has already been completely emptied by
                    earlier adventurers. The only exit is to the south.""",
                     [item['shield']]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


pretty = Prettier()

def refresh_display():
    pretty.clear_terminal()
    pretty.outline_info(player, player.current_room, 60)


username = 'Taran'
player = Player(username, room['outside'], playing=True, inv=[])

# Initial location info display
pretty.outline_info(player, player.current_room, 60)

while player.playing:

    # Getting player movement input
    player_input = input('Enter a cardinal direction: [n], [s], [e], [w], or [q] to quit\n')

    # Setting player input to lowercase and splitting it
    split_input = player_input.lower().split(' ')

    # Separate words to be parsed individually
    verb = split_input[0]
    obj = ''
    if len(split_input) == 2:
        obj = split_input[1]

    # Escape clause
    if verb == 'q':
        player.playing = False
        break

    # Check if input is a cardinal direction
    if verb in ['n', 's', 'e', 'w']:
        player.travel(f'{verb}_to', room)
        refresh_display()

    # Check if input is an action
    elif verb in ['i', 'take', 'drop']:
        if verb == 'i':
            player.toggle_inventory()
            refresh_display()

        # If current room contains specified item, then add it to inventory
        elif verb == 'take':
            try:
                if player.current_room.has_item(item[obj]):
                    player.take(item[obj])
                    refresh_display()
                else:
                    print('That item is not available')
            except KeyError:
                print('That item is not available')

        # If player has item, then drop it
        elif verb == 'drop':
            if player.has_item(item[obj]):
                player.drop(item[obj])
                refresh_display()
            else:
                print('You do not have this item!')

    else:
        print('Invalid command!')
