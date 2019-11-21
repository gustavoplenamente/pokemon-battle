import socket
import threading
import time

from api_settings import LOCALHOST, PORT
from api_utils import stringfy, dictionize
from settings.pokemon_configuration import bulbasaur, charmander, squirtle, pikachu
from game_logic.Player import Player
from game_logic.Pokemon import Pokemon


class SetPlayersThread(threading.Thread):
    clients = {}
    ready = {}

    pokemon_to_dict = {
        'Bulbasaur': bulbasaur,
        'Charmander': charmander,
        'Squirtle': squirtle,
        'Pikachu': pikachu
    }
    moves = {}

    def __init__(self, clientAddress, clientSocket):
        threading.Thread.__init__(self)
        self.csocket = clientSocket
        print("New connection added: ", clientAddress)
        self.clients[clientSocket] = clientAddress
        self.ready[clientSocket] = "not-ready"
        self.player = {}
        self.rivalSocket = None

    def run(self):

        addr = clientAddress[0]
        print("Connection from : ", addr)

        self.player = dictionize(self.csocket.recv(1024).decode())
        
        print(addr + " - Name: " + self.player["name"] + " - Pokemon: " + self.player["pokemon"])

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
        time.sleep(1)

        #self.rivalSocket.sendall(stringfy(self.player))
        print("Both are ready!\n")
        pokemon_obj = Pokemon(self.pokemon_to_dict[self.player['pokemon']])
        self.Player = Player(self.csocket, self.player['name'], pokemon_obj)

        time.sleep(2)

        print("Pokemon", self.player["pokemon"], "of", self.player["name"], "setted!")

        your_move = self.csocket.recv(1024).decode()
        print("Move", your_move, "was chosen by", self.clients[self.csocket])
        self.rivalSocket.sendall(your_move.encode())
        self.moves[self.csocket] = your_move
        print("Sent move to rival", self.clients[self.rivalSocket])

        while len(self.moves.keys()) == 1:
            time.sleep(1)
            
        print("Identified rival move")

        rival_move = self.moves[self.rivalSocket]

        if your_move > rival_move:
            self.csocket.sendall("victory".encode())
            print("Victory for", self.player["pokemon"], "of", self.player["name"], "(", self.clients[self.csocket], ")")
        elif your_move < rival_move:
            self.csocket.sendall("defeat".encode())
        else:
            self.csocket.sendall("draw".encode())
            print("Draw!")

        time.sleep(10)

if __name__ == "__main__":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((LOCALHOST, PORT))

    print("Server started")
    print("Waiting for client request..")

    server.listen(2)
    clientSock, clientAddress = server.accept()
    # threading.Thread(target=setPlayer).start()
    newthread = SetPlayersThread(clientAddress, clientSock)
    newthread.start()

    #server.listen(1)
    clientSock2, clientAddress2 = server.accept()
    newthread2 = SetPlayersThread(clientAddress2, clientSock2)
    newthread2.start()