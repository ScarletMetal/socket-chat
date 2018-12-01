
import json as pickle


class Message():

    def __init__(self, type, content="", args=()):
        self.type = type
        self.content = content
        self.args = args


def to_message(string) -> Message:
    d = pickle.loads(string)
    return Message(type=d['type'], content=d['content'], args=d['args'])

def to_string(message: Message) -> str :
    return pickle.dumps(message, default=lambda o: o.__dict__,
            sort_keys=True)
