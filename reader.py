class BufferReader:

    def __init__(self, source):
        self.source = lambda: source(1).decode()


    def read_line(self):
        last = ""
        line = ""

        while last != '\n':
            line += last
            last = self.source()
        return line