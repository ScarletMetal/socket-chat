import threading
from reader import BufferReader
from server.room import Room
import message
import sys

class ClientThread(threading.Thread):
    def __init__(self, client, chat):
        super().__init__()
        self.command_index = {
            "prompt": self.prompt,
            "lsrooms": self.ls_rooms,
            "exitroom": self.exit_room,
            "enterroom": self.enter_room,
            "mkroom": self.make_room,
            "setname": self.set_name,
        }
        self.message_index = {
            "room_exit": message.to_string(message.Message(type="MESSAGE", content="Client Exited")),
            "room_enter": message.to_string(message.Message(type="MESSAGE", content="Client Entered")),
            "prompt": message.to_string(message.Message(type="MESSAGE", content="hello, welcome to chat"))
        }
        self.client = client
        self.chat = chat

    def prompt(self, *args):
        self.client.message(self.message_index["prompt"])

    def set_name(self, *args):
        name = args[0]
        self.client.name = name

    def enter_room(self, *args):
        room = self.chat.get_room(args[0])
        if room is not None:
            self.client.enter_room(room)
            room.message(self.message_index['room_enter'])

    def exit_room(self, *args):
        room = self.client.room
        if room is not None:
            print("len room is {}".format(len(room)))
            self.client.exit_room()
            room.message(self.message_index['room_exit'],
                         exclude=self.client)
            if len(room) == 0:
                self.chat.delete_room(room)

    def make_room(self, *args):
        name = args[0]
        self.chat.add_room(Room(name))

    def ls_rooms(self, *args):
        self.client.message(message.to_string(
            message.Message(type="MESSAGE", content="The rooms that are available are :: " + self.chat.list_rooms())))

    def handle_message(self, msg):

        if msg.type == 'COMMAND':
            command_name = msg.args[0]
            if command_name in self.command_index.keys():
                self.command_index[command_name](*msg.args[1:])
        if msg.type == 'MESSAGE':
            new_msg = message.to_string(message.Message(type="MESSAGE",
                                                        content="{}:{}".format(self.client.name, msg.content)))
            if msg.args[0] == 'echo':
                self.client.room.message(new_msg)
                print("bla")
            else:
                self.client.forward(new_msg)

    def run(self):
        try:
            reader = BufferReader(self.client.sock.recv)
            while True:
                line = reader.read_line()
                print(line)
                msg = message.to_message(line)
                self.handle_message(msg)
        finally:
            sys.exit(0)


