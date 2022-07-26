import socket
import threading



# Assigning non-privileged port.
PORT = 5050
# Finding local host's IP address.
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)


