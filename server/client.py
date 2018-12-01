import socket
class Client:
    def __init__(self, sock):
        print(type(sock))
        self.sock = sock
        self.room = None
        self.name = ""

    def message(self, message):
        self.sock.send(message.encode())
        self.sock.send("\n".encode())

    def close(self):
        self.sock.close()

    def exit_room(self):
        if self.room is not None:
            self.room.remove(self)
            self.room = None

    def enter_room(self, room):
        self.room = room
        room.add(self)

    def forward(self, message):
        if self.room is not None:
            self.room.message(message, exclude=self)