from socket import socket
from game_logic.Pokemon import Pokemon


class Player:
    def __init__(self, conn: socket, name, pokemon: Pokemon):
        self.conn = conn
        self.name = name
        self.pokemon = pokemon
