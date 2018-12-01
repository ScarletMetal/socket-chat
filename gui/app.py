import tkinter
from gui.ui import GUI
import gui.network as network
from reader import BufferReader

def main():

    ip = input("Enter IP :: ")
    port = int(input("Enter Port :: "))

    sock = network.connect((ip, port))

    target = lambda s: sock.send("{}\n".format(s).encode())


    ui = GUI(target=target)
    listen_thread = network.ListenThread(BufferReader(sock.recv), ui)
    listen_thread.start()
    ui.request_prompt()
    ui.start()


if __name__ == '__main__':
    main()