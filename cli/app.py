import socket

from cli.input_thread import InputThread
from cli.listen_thread import ListenThread

def main():
    ip = input("Enter IP :: ")
    port = int(input("Enter Port :: "))
    address = (ip, port)

    sock = socket.socket()
    sock.connect(address)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 0)

    input_thread = InputThread(sock)
    listen_thread = ListenThread(sock)
    input_thread.start()
    listen_thread.start()

if __name__ == '__main__':
    main()