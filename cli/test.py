from cli.input_thread import InputThread
class test:
    def send(self, text):
        print(text.decode())

def test_input_thread():
    t = InputThread(test())
    t.start()


if __name__ == "__main__":
    test_input_thread()