import socket


def connect(address) -> socket.socket:
    sock = socket.socket()
    sock.connect(address)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 0)
    return sock