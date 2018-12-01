import threading
import message
class InputThread(threading.Thread):

    def __init__(self, socket):
        super().__init__()
        self.socket = socket

    def run(self):
        try:
            self.socket.send(((message.to_string(message.Message("COMMAND",
                                                                   args=["prompt"])))).encode())
            self.socket.send("\n".encode())
            while True:
                inp = input("Enter Line :: ")
                if inp[0] == '!':
                    inp = inp[1:]
                    inp = message.Message(type="COMMAND", args=inp.split(" "))
                else:
                    inp = message.Message(type="MESSAGE", content=inp)
                print(message.to_string(inp))
                self.socket.send((message.to_string(inp)).encode())
                self.socket.send('\n'.encode())
        finally:
            print("Error In Input Thread")


