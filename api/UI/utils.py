from api.UI.screen_config import bulbasaur_png, squirtle_png, charmander_png, pikachu_png
from api.UI.screen_config import pokemon_info

def choice(i, controller):
    if i==1:
        controller.show_frame("WaitOpponent", pathname = bulbasaur_png)
        controller.player_info["pokemon"] = "Bulbasaur"
    elif i==2:
        controller.show_frame("WaitOpponent", pathname = squirtle_png)
        controller.player_info["pokemon"] = "Squirtle"
    elif i==3:
        controller.show_frame("WaitOpponent", pathname = charmander_png)
        controller.player_info["pokemon"] = "Charmander"
    elif i==4:
        controller.show_frame("WaitOpponent", pathname = pikachu_png)
        controller.player_info["pokemon"] = "Pikachu"

def mapPathByPokeName(poke_name, mode):
    return pokemon_info[poke_name][mode]