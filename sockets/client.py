import socket
from settings import SERVER_ADDR, SERVER_PORT, MSG_LEN

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = SERVER_ADDR
port = SERVER_PORT
sock.connect((host, port))
while True:
    data = input("message: ")
    sock.send(data.encode())
    print("response: ", sock.recv(MSG_LEN).decode())
