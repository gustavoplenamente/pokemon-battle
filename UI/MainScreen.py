import tkinter as tk                # python 3
from tkinter import font as tkfont  # python 3

from UI.screen_config import no_img_path, pokeball_ico, app_geometry
from UI.screens import StartScreen, NameScreen, ChoosePokemon, WaitOpponent


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True, padx=20, pady=20)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartScreen, NameScreen, ChoosePokemon, WaitOpponent):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartScreen")

    def show_frame(self, page_name, pathname=no_img_path):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        if page_name == "WaitOpponent":
            frame.changeImg(pathname)
        frame.tkraise()

    def display(self):
        self.geometry(app_geometry)
        self.title("Pokémon Simulator")
        self.iconbitmap(pokeball_ico)
        self.mainloop()


if __name__ == "__main__":
    app = SampleApp()
    app.geometry(app_geometry)
    app.title("Pokémon Simulator")
    app.iconbitmap(pokeball_ico)
    app.mainloop()
