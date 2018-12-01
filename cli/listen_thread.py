import threading
import message
import sys
from reader import BufferReader

class ListenThread(threading.Thread):

    def __init__(self, socket):
        super().__init__()
        self.socket = socket

    def run(self):
        reader = BufferReader(self.socket.recv)

        try:
            while True:
                line = reader.read_line()
                msg = message.to_message(line)
                if msg.type == 'MESSAGE':
                    print("\n{}\n".format(msg.content))
                elif msg.type == "COMMAND":
                    if msg.args[0] == 'exit':
                        print("Exited Client")
                        sys.exit(0)

        finally:
            print("It Appears That The Server Was Closed")
            sys.exit(0)
