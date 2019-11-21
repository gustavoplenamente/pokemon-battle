import socket

from api.UI.MainScreen import SampleApp
from api.UI.BattleScreen import BattleApp
from api.api_settings import SERVER, PORT

from api import api_utils

from api.game_logic.Pokemon import Pokemon
from api.settings.pokemon_configuration import bulbasaur,charmander,squirtle,pikachu

pokemon_to_dict = {
    'Bulbasaur': bulbasaur,
    'Charmander': charmander,
    'Squirtle': squirtle,
    'Pikachu': pikachu
}

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))

setGameScreen = SampleApp()
setGameScreen.display()
setGameScreen.echo_player_info()
player_dict = setGameScreen.get_player_info()

client.sendall(api_utils.stringfy(player_dict).encode())

pokemon_obj = Pokemon(pokemon_to_dict[player_dict['pokemon']])

rival_dict = api_utils.dictionize(client.recv(1024).decode())

battleScreen = BattleApp(player_dict, rival_dict)

battleScreen.display()


