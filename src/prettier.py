import textwrap
from player import Player


class Prettier:

    def outline_info(self, player, room, width):

        wrapper = textwrap.TextWrapper(width)

        title_underline = ''
        desc_underline = ''

        for letter in range(len(room.name) + len('Location: ')):
            title_underline += '~'

        for letter in range(width):
            desc_underline += '~'

        title = f'{title_underline}\nLocation: {room.name}\n{title_underline}'
        description = f'{room.description}\n{desc_underline}'

        print(f'Hello, {player.name}! Inventory: {player.inventory}\n{title}\n{wrapper.fill(description)}')
        room.get_items()
