class Item:

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self):
        print(f'Picked up [{self.name}] - {self.description}')

    def on_drop(self):
        print(f'Dropped [{self.name}]')
