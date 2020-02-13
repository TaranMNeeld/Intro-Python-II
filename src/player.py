# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room, playing, inv=[]):
        self.name = name
        self.current_room = current_room
        self.playing = playing
        self.inventory = inv
