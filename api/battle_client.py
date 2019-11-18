import socket
import time

from api_settings import SERVER, PORT
from api_utils import dictionize
from UI.MainScreen import SampleApp

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))

while True:
    game_offer_encoded = client.recv(1024)
    game_offer = game_offer_encoded.decode()
    game_screen = SampleApp()
    game_screen.display()
    game_offer_answer = input(game_offer) # aperta o botão Play na tela
    client.sendall(game_offer_answer.encode())
    if game_offer_answer.lower() == "Play".lower():
        break

name_request = client.recv(1024).decode()

name = input(name_request)
client.sendall(name.encode())

pokemon_request = client.recv(1024).decode()

pokemon = input(pokemon_request)
client.sendall(pokemon.encode())

rival = dictionize( client.recv(1024).decode() )
print("Your rival is", rival["name"], "and his pokemon is", rival["pokemon"])


while True:
    time.sleep(1)
