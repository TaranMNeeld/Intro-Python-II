import textwrap


class Prettier:

    def outline_info(self, name, location, desc, width):

        wrapper = textwrap.TextWrapper(width)

        title_underline = ''
        desc_underline = ''

        for letter in range(len(location)):
            title_underline += '~'

        for letter in range(width):
            desc_underline += '~'

        title = f'{title_underline}\n{location}\n{title_underline}'
        description = f'{desc}\n{desc_underline}'

        print(f'Hello, {name}!\n{title}\n{wrapper.fill(description)}')
