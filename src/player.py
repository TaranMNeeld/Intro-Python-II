# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room, playing, inv):
        self.name = name
        self.current_room = current_room
        self.playing = playing
        self.inventory = inv
        self.inv_open = None

    def take(self, item):
        self.inventory.append(item)
        self.current_room.items.remove(item)
        item.on_take()

    def drop(self, item):
        self.current_room.items.append(item)
        self.inventory.remove(item)
        item.on_drop()

    def toggle_inventory(self):
        self.inv_open = not self.inv_open
        return self.inv_open

    def has_item(self, item):
        print(f'{item}, {self.inventory}')
        return item in self.inventory

    def travel(self, verb, room):
        # Setting the new room to a variable based off of the current room and player input
        new_room = getattr(self.current_room, verb)
        # Checking to see if the desired direction keeps you in the same room, or leads you to a new room
        if new_room is self.current_room:
            print('You cannot move in that direction!')
        else:
            self.current_room = new_room
            # Setting the player's location to the new room
            for key in room:
                if room[key] == new_room:
                    self.current_room = room[key]
