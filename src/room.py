# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.n_to = self
        self.s_to = self
        self.e_to = self
        self.w_to = self
        self.items = items

    def get_items(self):
        if len(self.items):
            return print(f'! You notice the following items: {[item.name for item in self.items]}\n'
                         f'Enter [take item_name] or...')
        else:
            return print('The location is empty...')

    def has_item(self, item):
        return item in self.items
