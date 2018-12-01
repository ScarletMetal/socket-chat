class Room:
    def __init__(self, name):
        self.clients = []
        self.name = name

    def __len__(self):
        return len(self.clients)

    def add(self, client):
        self.clients.append(client)

    def remove(self, client):
        self.clients.remove(client)

    def message(self, message, exclude=None):
        for client in self.clients:
            if client != exclude:
                client.message(message)