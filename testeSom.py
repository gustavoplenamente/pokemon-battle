from tkinter import *
import threading
import winsound


class Application:
    def __init__(self, master=None):
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.msg = Label(self.widget1, text="Primeiro widget")
        self.msg.pack ()

playSong = lambda: winsound.PlaySound('opening.wav', winsound.SND_FILENAME)
songThread = threading.Thread(target = playSong)
songThread.start()

root = Tk()
Application(root)
root.mainloop()