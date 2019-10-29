from tkinter import Tk, Frame, Label, Button, Entry, END, LEFT, BOTTOM, RIGHT
from PIL import ImageTk, Image

from UI.screen_config import name_screen_div1_pady, name_screen_div3_pady, name_screen_title, name_screen_img, \
    name_screen_playButton, name_screen_img_size


class NameScreen:
    def __init__(self, master=None):
        self.standardFont = ("Verdana", "16")
        self.div1 = Frame(master)
        self.div1["pady"] = name_screen_div1_pady
        self.div1.pack()

        self.div2 = Frame(master)
        self.div2.pack()

        self.div3 = Frame(master)
        self.div3["pady"] = name_screen_div3_pady
        self.div3.pack()

        self.title = Label(self.div1, text=name_screen_title)
        self.title["font"] = ("Verdana", "24", "bold")
        self.title.pack()

        screen_img = Image.open(name_screen_img).resize(name_screen_img_size, Image.ANTIALIAS)
        img = ImageTk.PhotoImage(screen_img)
        self.thumbnail = Label(self.div2, image=img)
        self.thumbnail.image = img
        self.thumbnail.pack()

        self.name_entry = Entry(self.div3)
        self.name_entry["width"] = 30
        self.name_entry["font"] = ("Verdana", "16")
        self.name_entry.insert(END, "Diga seu nome...")
        self.name_entry.pack(side=LEFT)

        self.playButton = Button(self.div3)
        self.playButton["text"] = name_screen_playButton
        self.playButton["width"] = 10
        self.playButton["font"] = ("Verdana", "16")
        self.playButton.pack(side=RIGHT)


if __name__ == "__main__":
    root = Tk()
    root.geometry("1000x600")
    # img = ImageTk.PhotoImage(Image.open("pikacapa.png"))
    # panel = Label(root, image = img)
    # panel.pack(side = "bottom", fill = "both", expand = "yes")
    root.title("Pokémon Simulator")
    # root.configure(background='blue')
    NameScreen(root)
    root.mainloop()