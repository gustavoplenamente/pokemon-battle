from tkinter import Tk, Frame, Label, Button
from PIL import ImageTk, Image
from UI.screen_config import welcome_screen_img, welcome_screen_title, welcome_screen_playButton, \
    welcome_screen_div3_pady, welcome_screen_div1_pady


class WelcomeScreen:
    def __init__(self, master=None):
        self.standardFont = ("Verdana", "16")
        self.div1 = Frame(master)
        self.div1["pady"] = welcome_screen_div1_pady
        self.div1.pack()

        self.div2 = Frame(master)
        self.div2.pack()

        self.div3 = Frame(master)
        self.div3["pady"] = welcome_screen_div3_pady
        self.div3.pack()

        self.title = Label(self.div1, text=welcome_screen_title)
        self.title["font"] = ("Verdana", "32", "bold")
        self.title.pack()

        screen_img = Image.open(welcome_screen_img)
        img = ImageTk.PhotoImage(screen_img)
        self.thumbnail = Label(self.div2, image=img)
        self.thumbnail.image = img
        self.thumbnail.pack()

        self.playButton = Button(self.div3)
        self.playButton["text"] = welcome_screen_playButton
        self.playButton["width"] = 10
        self.playButton["font"] = ("Verdana", "16")
        self.playButton.pack()

if __name__ == "__main__":
    root = Tk()
    root.geometry("1000x600")
    #img = ImageTk.PhotoImage(Image.open("pikacapa.png"))
    #panel = Label(root, image = img)
    #panel.pack(side = "bottom", fill = "both", expand = "yes")
    root.title("Pokémon Simulator")
    #root.configure(background='blue')
    WelcomeScreen(root)
    root.mainloop()