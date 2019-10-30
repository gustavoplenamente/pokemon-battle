from UI.screen_config import bulbasaur_png, squirtle_png, charmander_png, pikachu_png


def choice(i, controller):
    if i==1:
        controller.show_frame("WaitOpponent", pathname = bulbasaur_png)
    elif i==2:
        controller.show_frame("WaitOpponent", pathname = squirtle_png)
    elif i==3:
        controller.show_frame("WaitOpponent", pathname = charmander_png)
    elif i==4:
        controller.show_frame("WaitOpponent", pathname = pikachu_png)

