import socket
import threading
import time

from api_settings import LOCALHOST, PORT
from api_utils import stringfy
from settings.pokemon_configuration import bulbasaur, charmander, squirtle, pikachu
from game_logic.Player import Player
from game_logic.Pokemon import Pokemon
from game_logic.battle.battle_control import BattleController


class SetPlayersThread(threading.Thread):
    clients = {}
    ready = {}
    pokemons = {"1": "Bulbasaur", "2": "Squirtle",
                "3": "Charmander", "4": "Pikachu"}
    pokemon_to_dict = {
        'Bulbasaur': bulbasaur,
        'Charmander': charmander,
        'Squirtle': squirtle,
        'Pikachu': pikachu
    }
    moves = []

    def __init__(self, clientAddress, clientSocket, battle_judge: BattleController):
        threading.Thread.__init__(self)
        self.csocket = clientSocket
        print("New connection added: ", clientAddress)
        self.clients[clientSocket] = clientAddress
        self.ready[clientSocket] = "not-ready"
        self.player = {}
        self.rivalSocket = None
        self.battle_judge = battle_judge

    def run(self):

        addr = clientAddress[0]
        print("Connection from : ", addr)
        while True:
            game_offer = "Write \"Play\" if you want to play Pokemon Simulator!\n"
            self.csocket.sendall(game_offer.encode())
            game_offer_answer = self.csocket.recv(1024).decode()
            if game_offer_answer.lower() == "Play".lower():
                break

        print(addr + " wants to play!\n")
        name_request = "Say your name: "
        self.csocket.sendall(name_request.encode())
        name = self.csocket.recv(1024).decode()
        print(addr + " - Name: " + name)

        pokemon_request = """Choose a pokemon:
        (1) Bulbasaur\t(2) Squirtle\t(3) Charmander\t(4) Pikachu
        """
        self.csocket.sendall(pokemon_request.encode())
        pokemon_code = self.csocket.recv(1024).decode()
        pokemon = self.pokemons[pokemon_code]
        pokemon_obj = Pokemon(self.pokemon_to_dict[pokemon])
        print(addr + " - Pokemon: " + pokemon)

        self.player = {
            "name": name,
            "pokemon": pokemon
        }

        self.ready[self.csocket] = "ready"

        while len(self.clients) < 2:
            time.sleep(1)

        for client in self.clients:
            if self.csocket != client:
                while True:
                    self.rivalSocket = client
                    if self.ready[client] == "ready":
                        str_player = stringfy(self.player)
                        client.sendall(str_player.encode())
                        break
                    else:
                        time.sleep(1)

        pokemon_obj = Pokemon(self.pokemon_to_dict[self.player['pokemon']])
        self.Player = Player(self.csocket, self.player['name'], pokemon_obj)

        time.sleep(5)

        self.ready[self.csocket] = 'choose-move'

        while self.ready[self.rivalSocket] != 'choose-move':
            time.sleep(1)

        self.moves = pokemon_obj.moves

        move_request = """Choose a move:
        (1) %s\t(2) %s\t(3) %s\t(4) %s
        """% (self.moves[0], self.moves[1], self.moves[2], self.moves[3])
        self.csocket.sendall(move_request.encode())
        move_code = self.csocket.recv(1024).decode()
        move = self.moves[int(move_code)-1]
        print(addr + " - Move: " + move)

        self.ready[self.csocket] = 'waiting-rival'

        #
        player_obj = Player(self.csocket, name, pokemon_obj)
        self.battle_judge.addPlayer(player_obj)
        #

        while True:
            if self.ready[self.rivalSocket] == "waiting-rival":
                self.rivalSocket.sendall(move.encode())
                break
            else:
                time.sleep(1)

        time.sleep(5)








if __name__ == "__main__":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((LOCALHOST, PORT))

    print("Server started")
    print("Waiting for client request..")

    #
    battle_judge = BattleController()
    #

    server.listen(2)
    clientSock, clientAddress = server.accept()
    # threading.Thread(target=setPlayer).start()
    newthread = SetPlayersThread(clientAddress, clientSock)
    newthread.start()

    #server.listen(1)
    clientSock2, clientAddress2 = server.accept()
    newthread2 = SetPlayersThread(clientAddress2, clientSock2)
    newthread2.start()

