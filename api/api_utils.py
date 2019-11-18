import time

from api_settings import SERVER, PORT


def recv_function(client_socket, name):
    print("Starting thread " + name)
    while True:
        try:
            encoded_message, serverAddress = client_socket.recvfrom(1024)
            message = encoded_message.decode()
            print(message)
        except Exception as e:
            print("\nExiting...")
            client_socket.close()
            break


def send_function(client_socket, name):
    time.sleep(0.5)
    print("Starting thread " + name)
    while True:
        try:
            message = input("You: ")
            encoded_message = message.encode()
            client_socket.sendto(bytes(encoded_message), (SERVER, PORT))
            time.sleep(0.5)
        except KeyboardInterrupt:
            print("\nExiting...")
            client_socket.close()
            break

def stringfy2(dictionary):
    stringfied = "{"
    for key in dictionary.keys():
        stringfied += key + ":" + dictionary[key] + ","
    stringfied = stringfied[:-1] + "}"
    return stringfied

def stringfy(dictionary):
    result = ""
    for key in dictionary.keys():
        #print("in utils key : value", key, dictionary[key])
        result += key + ":" + dictionary[key] + ","
    result = result[:-1]
    return result


def dictionize(s):
    d = {}
    keys_values = s.split(",")
    for key_value_str in keys_values:
        key_value = key_value_str.split(":")
        d[key_value[0]] = key_value[1]

    return d