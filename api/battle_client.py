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
    #game_screen = SampleApp()
    #game_screen.display()
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
#print(rival)
print("Your rival is", rival["name"], "and his pokemon is", rival["pokemon"])

move_request = client.recv(1024).decode()

move = input(move_request)

if pokemon == '1':
    #buba
    moves = {"1": "Razor Leaf", "2": "Vine Whip",
         "3": "Tackle", "4": "Poison Powder"}

elif pokemon == '2':
    #sk
    moves = {"1": "Pound", "2": "Water Gun",
             "3": "Bubblebeam", "4": "Bash Skull"}

elif pokemon == '3':
    #char

    moves = {"1": "Scratch", "2": "Ember",
             "3": "Flamethrower", "4": "Bite"}

else:
    #pika
    moves = {"1": "Thundershock", "2": "Quick Attack",
             "3": "Iron Tail", "4": "Slam"}



client.sendall(move.encode())
rival_move = client.recv(1024).decode()
print(rival["name"] + "'s pokemon " + rival["pokemon"] + " choose " + rival_move + "!")

move = moves[move]

if move > rival_move:
    print("You Win!")
elif move == rival_move:
    print("Draw!")
else:
    print("You lose!")

time.sleep(2)
