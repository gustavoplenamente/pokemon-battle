from socket import socket, AF_INET, SOCK_STREAM
from typing import List
from settings import MSG_LEN, SERVER_PORT, SERVER_ADDR

server = socket(AF_INET, SOCK_STREAM)
server.bind((SERVER_ADDR, SERVER_PORT))
print("Server started")
print("Waiting for client request..")

NUM_PLAYERS = 2
clients: List[socket] = []
client_addrs = []

for i in range(NUM_PLAYERS):
    server.listen(1)
    client_sock, client_addr = server.accept()
    clients.append(client_sock)
    client_addrs.append(client_addr)

while True:
    for i in range(NUM_PLAYERS):
        data = clients[i].recv(MSG_LEN)
        # Process data
        clients[i].send(data)
