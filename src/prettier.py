import textwrap
import os
from player import Player


class Prettier:

    def outline_info(self, player, room, width):

        wrapper = textwrap.TextWrapper(width)

        title_underline = ''
        desc_underline = ''

        empty = []

        for letter in range(len(room.name) + len('Location: ')):
            title_underline += '~'

        for letter in range(width):
            desc_underline += '~'

        title = f'{title_underline}\nLocation: {room.name}\n{title_underline}'
        description = f'{room.description}\n{desc_underline}'

        print(f'Hello, {player.name}! Enter [i] to open inventory:'
              f'{player.inventory if player.inv_open else empty}\n'
              f'{title}\n{wrapper.fill(description)}')
        room.get_items()

    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')