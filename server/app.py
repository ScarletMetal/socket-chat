import socket

from server.chat import Chat
from server.client import Client
from server.client_thread import ClientThread


def main():
    chat = Chat()
    address = ('0.0.0.0', 8048)
    server_socket = socket.socket()
    server_socket.bind(address)
    server_socket.listen(100)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print('started on address {}'.format(address))
    try:
        while True:
            sock, ad = server_socket.accept()
            client = Client(sock)
            thread = ClientThread(client, chat)
            thread.start()
    finally:
        server_socket.close()


if __name__ == '__main__':
    main()
