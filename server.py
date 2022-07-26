import socket
import threading



# Assigning non-privileged port.
PORT = 5050
# Finding local host's IP address.
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

# Creating a new socket (AF_INET argument  determines  family of # addresses that this
# socket can  communicate with (in this case, Internet Protocol v4 addresses).
# SOCK_STREAM is a transmission mechanism (in this case, two-way byte streams of data).
# Anything that connects to the specified IP & port now, will hit that socket.
server_socket = socket.socket(socket.AF_INET, sockets.SOCK_STREAM)

