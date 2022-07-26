import socket


# Setting up Server IP address and port constants
PORT = 5050
SERVER = "192.168.0.44"
ADDR = (SERVER, PORT)

FORMAT = "utf-8"
DISCONNECT_MESSAGE = "DISCONNECT"
HEADER = 50
# Setting up the socket ofr the client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connecting to the server
client.connect(ADDR)

def send(msg):
    """
    User will input a message and it will be sent to the server
    param msg: User's input in form of dictionary or text file
    """
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    # Pad the message to make the lenght equal 50 bytes (HEADER)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

