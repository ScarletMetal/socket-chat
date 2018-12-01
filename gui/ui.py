import tkinter
from message import Message
import message

class GUI:

    def __init__(self, target=lambda s: print(s)):
        self.top = tkinter.Tk()
        self.list = tkinter.Listbox(self.top, width=100)
        self.list_index = 1

        self.message_label = tkinter.Label(self.top, text = "Enter Your Message")
        self.message_entry = tkinter.Entry(self.top, bd = 5)
        self.message_button = tkinter.Button(self.top, text = "send", command=self.send_message)

        self.target = target
        # self.top.bind('<Return>', self.send_on_enter)


    def send_on_enter(self, *args):
        try:
            self.send_message()
        except Exception as e:
            print(e)
            pass

    def send_message(self):
        text = self.message_entry.get()

        msg_type = "MESSAGE"
        args = ["echo"]
        content = text

        if text[0] == "!":
            msg_type = "COMMAND"
            args = text[1:].split(' ')
            content = ""

        msg = Message(msg_type, args=args, content=content)
        self.target(message.to_string(msg))
        self.message_entry.delete(0, len(text))



    def show_widgets(self):
        self.list.pack()
        self.message_label.pack(side=tkinter.LEFT)
        self.message_button.pack(side=tkinter.RIGHT)
        self.message_entry.pack(side=tkinter.RIGHT)


    def append_message(self, msg):
        self.list.insert(self.list_index, msg)
        self.list.pack()
        self.list_index += 1

    def request_prompt(self):
        msg = Message(type="COMMAND", args=["prompt"])
        self.target(message.to_string(msg))


    def start(self):
        self.show_widgets()
        self.top.mainloop()

    def quit(self):
        self.top.quit()