import socket

from api.UI.MainScreen import SampleApp
from api.api_settings import SERVER, PORT

from api import api_utils

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))

setGameScreen = SampleApp()
setGameScreen.display()
setGameScreen.echo_player_info()
player_dict = setGameScreen.get_player_info()

client.sendall(api_utils.stringfy(player_dict).encode())


