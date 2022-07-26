import socket


# Setting up Server IP address and port constants
PORT = 5050
SERVER = "192.168.0.44"
ADDR = (SERVER, PORT)

FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

# Setting up the socket ofr the client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connecting to the server
client.connect(ADDR)
