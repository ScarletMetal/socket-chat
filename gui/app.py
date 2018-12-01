import tkinter
from gui.gui import GUI
import gui.network as network

def main():

    ip = input("Enter IP :: ")
    port = input("Enter Port :: ")

    sock = network.connect((ip, port))

    target = lambda s: sock.send(s.encode())

    gui = GUI(target=target)
    gui.start()


if __name__ == '__main__':
    main()