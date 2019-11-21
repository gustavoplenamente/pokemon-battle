import tkinter as tk
from PIL import Image, ImageTk
import winsound
import threading

from api.UI.screen_config import choose_pokemon_title, welcome_screen_playButton, name_screen_playButton, name_screen_title, \
    name_screen_img, name_screen_img_size, welcome_screen_title, welcome_screen_img, pikachu_png, charmander_png, \
    bulbasaur_png, squirtle_png
from api.UI.utils import choice

from api.UI.screen_config import no_img_path


class StartScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.standardFont = ("Verdana", "16")

        self.div1 = tk.Frame(self)
        #self.div1["pady"] = welcome_screen_div1_pady
        self.div1.pack()

        self.div2 = tk.Frame(self)
        self.div2.pack()

        self.div3 = tk.Frame(self)
        #self.div3["pady"] = welcome_screen_div3_pady
        self.div3.pack(side=tk.BOTTOM)

        self.title = tk.Label(self.div1, text=welcome_screen_title)
        self.title["font"] = ("Verdana", "32", "bold")
        self.title.pack()

        screen_img = Image.open(welcome_screen_img)
        img = ImageTk.PhotoImage(screen_img)
        self.thumbnail = tk.Label(self.div2, image=img)
        self.thumbnail.image = img
        self.thumbnail.pack()

        self.playButton = tk.Button(self.div3)
        self.playButton["text"] = welcome_screen_playButton
        self.playButton["width"] = 10
        self.playButton["font"] = ("Verdana", "16")
        
        playSong = lambda: winsound.PlaySound('opening.wav', winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)
        songThread = threading.Thread(target = playSong)
            
        self.playButton["command"] = lambda: controller.show_frame("NameScreen") or songThread.start()
        self.playButton.pack()


class NameScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.standardFont = ("Verdana", "16")
        self.div1 = tk.Frame(self)
        #self.div1["pady"] = name_screen_div1_pady
        self.div1.pack()

        self.div2 = tk.Frame(self)
        self.div2.pack()

        self.div3 = tk.Frame(self)
        #self.div3["pady"] = name_screen_div3_pady
        self.div3.pack(side=tk.BOTTOM)

        self.title = tk.Label(self.div1, text=name_screen_title)
        self.title["font"] = ("Verdana", "24", "bold")
        self.title.pack()

        screen_img = Image.open(name_screen_img).resize(name_screen_img_size, Image.ANTIALIAS)
        img = ImageTk.PhotoImage(screen_img)
        self.thumbnail = tk.Label(self.div2, image=img)
        self.thumbnail.image = img
        self.thumbnail.pack()

        self.name_entry = tk.Entry(self.div3)
        self.name_entry["width"] = 30
        self.name_entry["font"] = ("Verdana", "16")
        self.name_entry.insert(tk.END, "Diga seu nome...")
        self.name_entry.bind('<FocusIn>', self.clearEntry)
        self.name_entry.pack(side=tk.LEFT)

        self.playButton = tk.Button(self.div3)
        self.playButton["text"] = "Ok"
        self.playButton["width"] = 10
        self.playButton["font"] = ("Verdana", "16")
        self.playButton["command"] = lambda: controller.show_frame("ChoosePokemon")
        self.playButton.pack(side=tk.RIGHT)

        #self.event_add

    def clearEntry(self, event):
        self.playButton["text"]= name_screen_playButton

    def getName(self):
        return self.name_entry.get()


class ChoosePokemon(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.standardFont = ("Verdana", "16")

        self.div1 = tk.Frame(self)
        #self.div1["pady"] = welcome_screen_div1_pady
        self.div1.grid(row=0, column=0, sticky="nswe", columnspan=4)

        self.div2 = tk.Frame(self)
        self.div3 = tk.Frame(self)
        self.div4 = tk.Frame(self)
        self.div5 = tk.Frame(self)

        self.div2.grid(row=1,column=0, sticky="nswe", rowspan=4)
        self.div3.grid(row=1, column=1, sticky="nswe", rowspan=4)
        self.div4.grid(row=1, column=2, sticky="nswe", rowspan=4)
        self.div5.grid(row=1, column=3, sticky="nswe", rowspan=4)

        self.title = tk.Label(self.div1, text=choose_pokemon_title)
        self.title["font"] = ("Verdana", "24", "bold")
        self.title.pack()

        screen_img1 = Image.open(bulbasaur_png).resize((150,150), Image.ANTIALIAS)
        img1 = ImageTk.PhotoImage(screen_img1)
        self.img1 = tk.Label(self.div2, image=img1)
        self.img1.image = img1
        self.img1.pack(fill="both", expand=True)

        screen_img2 = Image.open(squirtle_png).resize((200,200), Image.ANTIALIAS)
        img2 = ImageTk.PhotoImage(screen_img2)
        self.img2 = tk.Label(self.div3, image=img2)
        self.img2.image = img2
        self.img2.pack(fill="both", expand=True)

        screen_img3 = Image.open(charmander_png).resize((150,150), Image.ANTIALIAS)
        img3 = ImageTk.PhotoImage(screen_img3)
        self.img3 = tk.Label(self.div4, image=img3)
        self.img3.image = img3
        self.img3.pack(fill="both", expand=True)

        screen_img4 = Image.open(pikachu_png).resize((200,200), Image.ANTIALIAS)
        img4 = ImageTk.PhotoImage(screen_img4)
        self.img4 = tk.Label(self.div5, image=img4)
        self.img4.image = img4
        self.img4.pack(fill="both", expand=True)

        #self.pokemon_choice = -1

        self.button1 = tk.Button(self.div2, text = "Bulbasaur", width = 10, command=lambda:choice(1, controller))
        self.button1.pack(side=tk.BOTTOM)

        self.button2 = tk.Button(self.div3, text = "Squirtle", width = 10, command=lambda:choice(2, controller))
        self.button2.pack(side=tk.BOTTOM)

        self.button3 = tk.Button(self.div4, text = "Charmander", width = 10, command=lambda:choice(3, controller))
        self.button3.pack(side=tk.BOTTOM)

        self.button4 = tk.Button(self.div5, text = "Pikachu", width = 10, command=lambda:choice(4, controller))
        self.button4.pack(side=tk.BOTTOM)


class WaitOpponent(tk.Frame):
    def __init__(self, parent, controller, pathname = no_img_path):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.standardFont = ("Verdana", "16")
        self.div1 = tk.Frame(self)
        self.div1.pack(fill="both", expand=True)

        self.img_path = pathname

        screen_img = Image.open(self.img_path).resize((250,250), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(screen_img)
        self.img = tk.Label(self.div1, image=img)
        self.img.image = img
        self.img.pack(fill="both", expand=True)

        self.msg = tk.Label(self.div1, text = "Aguarde por um jogador...", font = self.standardFont)
        self.msg.pack()

        self.div2 = tk.Frame(self)
        self.div2.pack(fill="both", expand=True)

        self.quitButton = tk.Button(self.div2)
        self.quitButton["text"] = "Batalha!"
        self.quitButton["width"] = 10
        self.quitButton["font"] = ("Verdana", "16")

        self.quitButton["command"] = lambda: controller.set_player_state('ready') or controller.destroy()
        self.quitButton.pack()

    def changeImg(self, img_path):
        self.img_path = img_path
        screen_img = Image.open(self.img_path).resize((250, 250), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(screen_img)
        self.img.configure(image = img)
        self.img.image = img


if __name__ == "__main__":
    pass
