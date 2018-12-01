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

    try:
        ui.start()

    except KeyboardInterrupt:
        print("keyboard")
        sock.close()
        ui.quit()

    finally:
        print("closed")

def test_ui():
    ui = GUI()
    ui.start()

if __name__ == '__main__':
    main()