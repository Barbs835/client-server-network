import socket
import pickle
import json
import sys
from dict2xml import dict2xml
from cryptography.fernet import Fernet



# Setting up Server IP address and port constants
PORT = 5050
# if server is not a local host, replace with IP address string
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "DISCONNECT"
HEADER = 1024
crypt = Fernet('sqcyNL5kz2mxWb1KL2QSZWY-GCERE-scEgWBbvq9CCk=')
dictionary = {}
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def connect_to_server():
    try:
        # Connecting to the server
        client_socket.connect(ADDR)
        print('[CONNECTED]')
        return True
    except ConnectionRefusedError:
        print(f"No connection could be made. Check if there is a server running at IP, Port: {ADDR}")
        return False


def client_disconnect():
    """
    Client closes successful connection.
    """
    if client_socket is not None:
        client_socket.send(f"CLIENT HAS DISCONNECTED".encode())
        client_socket.close()
        print("Client has disconnected")

connect_to_server()
client_disconnect()