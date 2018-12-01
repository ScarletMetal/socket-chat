import functools

class Chat:
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        if not room in self.rooms:
            self.rooms.append(room)

    def get_room(self, name):
        for room in self.rooms:
            if room.name == name:
                return room
        return None

    def delete_room(self, room):
        self.rooms.remove(room)

    def list_rooms(self):
        ls = ""
        for room in self.rooms:
            ls += room.name + " "
        print("ls is {}".format(ls))
        return ls
