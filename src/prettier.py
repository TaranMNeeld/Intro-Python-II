import textwrap
import os
from player import Player


class Prettier:

    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def outline_info(self, player, room, width):
        self.clear_terminal()
        wrapper = textwrap.TextWrapper(width)

        title_underline = ''
        desc_underline = ''

        open_option = 'Enter [i] to open inventory:'
        close_option = 'Enter [i] to close inventory:'

        inventory = []

        for item in player.inventory:
            inventory.append(item.name)

        for letter in range(len(room.name) + len('Location: ')):
            title_underline += '~'

        for letter in range(width):
            desc_underline += '~'

        title = f'{title_underline}\nLocation: {room.name}\n{title_underline}'
        description = f'{room.description}\n{desc_underline}'

        print(f'Hello, {player.name}! {close_option if player.inv_open else open_option}'
              f'{inventory if player.inv_open else "[]"}\n'
              f'{"! Enter [drop item_name] to add item to room" if player.inv_open else ""}\n'
              f'{title}\n{wrapper.fill(description)}')
        room.get_items()
