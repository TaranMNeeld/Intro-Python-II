import os
import textwrap
from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
                    passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
                    into the darkness. Ahead to the north, a light flickers in
                    the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
                    to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
                    chamber! Sadly, it has already been completely emptied by
                    earlier adventurers. The only exit is to the south."""),
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


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


player = Player('treasure', playing=1)

possible_moves = {
    'n': 'n_to',
    's': 's_to',
    'e': 'e_to',
    'w': 'w_to'
}

while player.playing == 1:

    player_input = input('Enter a cardinal direction: [n], [s], [e], [w], or [q] to quit\n')
    move_input = player_input.lower()

    if move_input == 'q':
        player.playing = 0
        break

    if move_input in possible_moves:
        current_room = getattr(room[player.room], possible_moves[move_input])
        if current_room.name == room[player.room].name:
            clear_terminal()
            print('You cannot move in that direction!')
        else:
            clear_terminal()
            print(f'{current_room.name} - \n{textwrap.fill(current_room.description, width=40)}')
            for key in room:
                if room[key] == current_room:
                    player.room = key
    else:
        clear_terminal()
        print('Invalid direction!')
