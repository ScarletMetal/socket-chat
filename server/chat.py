import functools

class Chat:
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        for r in self.rooms:
            if r.name == room.name:
                return
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
