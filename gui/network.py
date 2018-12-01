import socket
import threading
import message

class ListenThread(threading.Thread):

    def __init__(self, reader, ui):
        super().__init__()
        self.reader = reader
        self.ui = ui

    def run(self):

        try:
            while True:
                msg = message.to_message(self.reader.read_line())

                if msg.type == "COMMAND" and msg.args[0] == "exit":
                    self.ui.quit()
                else:
                    self.ui.append_message(msg.content)

        finally:
            print("connection was closed")





def connect(address) -> socket.socket:
    sock = socket.socket()
    sock.connect(address)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 0)
    return sock
