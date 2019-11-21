import tkinter as tk
from PIL import Image, ImageTk
import winsound
import threading

from api.UI.screen_config import choose_pokemon_title, welcome_screen_playButton, name_screen_playButton, name_screen_title, \
    name_screen_img, name_screen_img_size, welcome_screen_title, welcome_screen_img, pikachu_png, charmander_png, \
    bulbasaur_png, squirtle_png
from api.UI.utils import choice

from api.UI.screen_config import no_img_path

from api.UI.utils import mapPathByPokeName

class WaitRivalScreen(tk.Frame):
    def __init__(self, parent, controller, pathname = no_img_path, pathname2 = no_img_path):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        #self.standardFont = ("Verdana", "16")
        self.div1 = tk.Frame(self)
        self.div1.pack(fill="both", expand=True)

        self.img_path = mapPathByPokeName(controller.player_info["pokemon"].lower(), "wait_img")
        self.img_path2 = mapPathByPokeName(controller.rival_info["pokemon"].lower(), "wait_img")

        screen_img = Image.open(self.img_path).resize((250,250), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(screen_img)
        self.img = tk.Label(self.div1, image=img)
        self.img.image = img
        self.img.pack(fill="both", expand=True, side = tk.LEFT)

        self.msg = tk.Label(self.div1, text = "\"" + controller.player_info["name"] + "\" Vs \""
                                            + controller.rival_info["name"] + "\"", font = ("Verdana", "24"))
        self.msg.pack(side = tk.LEFT)

        screen_img2 = Image.open(self.img_path2).resize((250,250), Image.ANTIALIAS)
        img2 = ImageTk.PhotoImage(screen_img2)
        self.img2 = tk.Label(self.div1, image=img2)
        self.img2.image = img2
        self.img2.pack(fill="both", expand=True, side = tk.LEFT)

        self.div2 = tk.Frame(self)
        self.div2.pack(fill="both", expand=True)

        self.battleButton = tk.Button(self.div2)
        self.battleButton["text"] = "A batalha vai começar!"
        self.battleButton["width"] = 30
        self.battleButton["font"] = ("Verdana", "16")

        self.battleButton["command"] = lambda: controller.set_player_state('choose-move') or controller.show_frame("ChooseMoveScreen")
        self.battleButton.pack()



    def changeImg(self, img_path, img_path2):
        self.img_path = img_path
        screen_img = Image.open(self.img_path).resize((250, 250), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(screen_img)
        self.img.configure(image = img)
        self.img.image = img

        self.img_path2 = img_path2
        screen_img2 = Image.open(self.img_path2).resize((250, 250), Image.ANTIALIAS)
        img2 = ImageTk.PhotoImage(screen_img2)
        self.img2.configure(image = img2)
        self.img2.image = img2


class ChooseMoveScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        #self.standardFont = ("Verdana", "16")
        self.div1 = tk.Frame(self)
        self.div1.pack(fill="both", expand=True, side = tk.LEFT)

        self.div2 = tk.Frame(self)
        self.div2.pack(fill="both", expand=True, side = tk.LEFT)

        self.div3 = tk.Frame(self)
        self.div3.pack(fill="both", expand=True, side = tk.LEFT)

        self.div11 = tk.Frame(self.div1)
        self.div11.pack(fill="both", expand=True, side = tk.TOP)

        self.div31 = tk.Frame(self.div3)
        self.div31.pack(fill="both", expand=True, side = tk.BOTTOM)

        self.img_path = mapPathByPokeName(controller.player_info["pokemon"].lower(), "wait_img")
        self.img_path2 = mapPathByPokeName(controller.rival_info["pokemon"].lower(), "wait_img")

        screen_img = Image.open(self.img_path).resize((250,250), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(screen_img)
        self.img = tk.Label(self.div11, image=img)
        self.img.image = img
        self.img.pack(fill="both", expand=True, side = tk.BOTTOM)

        self.msg = tk.Label(self.div2, text = "\"" + controller.player_info["name"] + "\"\nVs\n\""
                                            + controller.rival_info["name"] + "\"", font = ("Verdana", "18"))
        self.msg.pack(side = tk.TOP)

        self.moves = tk.Label(self.div2, text = "Escolha um golpe!", font = ("Verdana", "14"))
        self.moves.pack(side = tk.BOTTOM)

        self.move1 = tk.Button(self.div2)
        self.move1["text"] = controller.pokemon.moves[0]
        self.move1["width"] = 25
        self.move1["font"] = ("Verdana", "16")

        self.move1["command"] = lambda: controller.set_player_state('wait-move') \
                                        or controller.set_cur_move(controller.pokemon.moves[0]) \
                                        or controller.show_frame("WaitMoveScreen")
                                        
        self.move1.pack(side = tk.BOTTOM)

        self.move2 = tk.Button(self.div2)
        self.move2["text"] = controller.pokemon.moves[1]
        self.move2["width"] = 25
        self.move2["font"] = ("Verdana", "16")

        self.move2["command"] = lambda: controller.set_player_state('wait-move') \
                                        or controller.set_cur_move(controller.pokemon.moves[1]) \
                                        or controller.show_frame("WaitMoveScreen")
        self.move2.pack(side = tk.BOTTOM)

        self.move3 = tk.Button(self.div2)
        self.move3["text"] = controller.pokemon.moves[2]
        self.move3["width"] = 25
        self.move3["font"] = ("Verdana", "16")

        self.move3["command"] = lambda: controller.set_player_state('wait-move') \
                                        or controller.set_cur_move(controller.pokemon.moves[2]) \
                                        or controller.show_frame("WaitMoveScreen")
        self.move3.pack(side = tk.BOTTOM)

        self.move4 = tk.Button(self.div2)
        self.move4["text"] = controller.pokemon.moves[3]
        self.move4["width"] = 25
        self.move4["font"] = ("Verdana", "16")

        self.move4["command"] = lambda: controller.set_player_state('wait-move') \
                                        or controller.set_cur_move(controller.pokemon.moves[3]) \
                                        or controller.show_frame("WaitMoveScreen")
        self.move4.pack(side = tk.BOTTOM)
        

        screen_img2 = Image.open(self.img_path2).resize((250,250), Image.ANTIALIAS)
        img2 = ImageTk.PhotoImage(screen_img2)
        self.img2 = tk.Label(self.div31, image=img2)
        self.img2.image = img2
        self.img2.pack(fill="both", expand=True, side = tk.TOP)

class WaitMoveScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        #self.standardFont = ("Verdana", "16")
        self.div1 = tk.Frame(self)
        self.div1.pack(fill="both", expand=True, side = tk.LEFT)

        self.div2 = tk.Frame(self)
        self.div2.pack(fill="both", expand=True, side = tk.LEFT)

        self.div3 = tk.Frame(self)
        self.div3.pack(fill="both", expand=True, side = tk.LEFT)

        self.div11 = tk.Frame(self.div1)
        self.div11.pack(fill="both", expand=True, side = tk.TOP)

        self.div31 = tk.Frame(self.div3)
        self.div31.pack(fill="both", expand=True, side = tk.BOTTOM)

        self.img_path = mapPathByPokeName(controller.player_info["pokemon"].lower(), "wait_img")
        self.img_path2 = mapPathByPokeName(controller.rival_info["pokemon"].lower(), "wait_img")

        screen_img = Image.open(self.img_path).resize((250,250), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(screen_img)
        self.img = tk.Label(self.div11, image=img)
        self.img.image = img
        self.img.pack(fill="both", expand=True, side = tk.BOTTOM)

        self.msg = tk.Label(self.div2, text = "\"" + controller.player_info["name"] + "\"\nVs\n\""
                                            + controller.rival_info["name"] + "\"", font = ("Verdana", "18"))
        self.msg.pack(side = tk.TOP)

        self.moves = tk.Label(self.div2, text = controller.player_info['pokemon'] + " utilizou " + controller.get_cur_move() + "!", font = ("Verdana", "14"))
        self.moves.pack(side = tk.BOTTOM)
        

        screen_img2 = Image.open(self.img_path2).resize((250,250), Image.ANTIALIAS)
        img2 = ImageTk.PhotoImage(screen_img2)
        self.img2 = tk.Label(self.div31, image=img2)
        self.img2.image = img2
        self.img2.pack(fill="both", expand=True, side = tk.TOP)



class NaoSeiScreen(tk.Frame):
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

        self.button1 = tk.Button(self.div2, text = "Bulbasaur", width = 10, command=lambda:choice(1, controller))
        self.button1.pack(side=tk.BOTTOM)

        self.button2 = tk.Button(self.div3, text = "Squirtle", width = 10, command=lambda:choice(2, controller))
        self.button2.pack(side=tk.BOTTOM)

        self.button3 = tk.Button(self.div4, text = "Charmander", width = 10, command=lambda:choice(3, controller))
        self.button3.pack(side=tk.BOTTOM)

        self.button4 = tk.Button(self.div5, text = "Pikachu", width = 10, command=lambda:choice(4, controller))
        self.button4.pack(side=tk.BOTTOM)


class WaaitMoveScreen(tk.Frame):
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

        self.quitButton["command"] = lambda: controller.set_player_state('ready') or controller.quit()
        self.quitButton.pack()

    def changeImg(self, img_path):
        self.img_path = img_path
        screen_img = Image.open(self.img_path).resize((250, 250), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(screen_img)
        self.img.configure(image = img)
        self.img.image = img

class SeeNadaScreen(tk.Frame):
    def __init__(self, parent, controller, pathname = no_img_path):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.standardFont = ("Verdana", "16")
        self.div1 = tk.Frame(self)
        self.div1.pack(fill="both", expand=True)

        self.img_path = pathname

class EndBattleScreen(tk.Frame):
    def __init__(self, parent, controller, pathname = no_img_path):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.standardFont = ("Verdana", "16")
        self.div1 = tk.Frame(self)
        self.div1.pack(fill="both", expand=True)

        self.img_path = pathname

if __name__ == "__main__":
    pass
