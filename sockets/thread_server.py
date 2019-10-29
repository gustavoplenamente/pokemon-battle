from socket import socket, AF_INET, SOCK_STREAM
from typing import List
from settings.settings import MSG_LEN, SERVER_PORT, SERVER_ADDR

server = socket(AF_INET, SOCK_STREAM)
server.bind((SERVER_ADDR, SERVER_PORT))
print("Server started")
print("Waiting for client request..")

NUM_PLAYERS = 2
clients: List[socket] = []
client_addrs = []
