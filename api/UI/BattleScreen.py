import tkinter as tk                # python 3
from tkinter import font as tkfont  # python 3
import threading

from api.UI import screen_config
from api.UI import battle_screens

from api.UI.utils import mapPathByPokeName

import winsound

from api.UI.utils import pokemon_to_dict
from api.game_logic.Pokemon import Pokemon

class BattleApp(tk.Tk):

    def __init__(self, player, rival, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # store player info
        self.player_info = player
        self.rival_info = rival
        self.pokemon = Pokemon(pokemon_to_dict[self.player_info['pokemon']])
        self.cur_move = 'struggle'

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True, padx=20, pady=20)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (battle_screens.WaitRivalScreen, battle_screens.ChooseMoveScreen, battle_screens.WaitMoveScreen):
        #for F in (screens.StartScreen, screens.NameScreen, screens.ChoosePokemon, screens.WaitOpponent):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("WaitRivalScreen")

    def show_frame(self, page_name, pathname=screen_config.no_img_path):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        #if page_name == "WaitRivalScreen":
        #    frame.changeImg(mapPathByPokeName(self.player_info["pokemon"].lower(), "wait_img"),
        #                    mapPathByPokeName(self.rival_info["pokemon"].lower(), "wait_img"))

        frame.tkraise()

    def display(self):
        self.geometry(screen_config.app_geometry)
        self.title("Pokémon Simulator")
        self.iconbitmap(screen_config.pokeball_ico)
        
        playSong = lambda: winsound.PlaySound('battle.wav', winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)
        songThread = threading.Thread(target = playSong)
        songThread.start()
        
        self.mainloop()

    def echo_player_info(self):
        print("Name :", self.player_info['name'], ", Pokémon :", self.player_info['pokemon'], "->", self.player_info['state'])

    def get_player_info(self):
        return self.player_info

    def set_player_state(self, state):
        self.player_info["state"] = state

    def set_cur_move(self, move):
        self.cur_move = move

    def get_cur_move(self):
        return self.cur_move


if __name__ == "__main__":
    app = BattleApp({'name':'Ash', 'pokemon':'Ghost', 'state':'not-ready'},
                    {'name':'Gary', 'pokemon':'Ghost', 'state':'not-ready'})
    app.geometry(screen_config.app_geometry)
    app.title("Pokémon Simulator")
    app.iconbitmap(screen_config.pokeball_ico)
    app.mainloop()
