import socket
import threading



# Setting up constants.

# Assigning non-privileged port.
PORT = 5050
# Finding local host's IP address.
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
# Length of message in bytes
HEADER = 50
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

# Creating a new socket (AF_INET argument  determines  family of # addresses that this
# socket can  communicate with (in this case, Internet Protocol v4 addresses).
# SOCK_STREAM is a transmission mechanism (in this case, two-way byte streams of data).
# Anything that connects to the specified IP & port now, will hit that socket.
server_socket = socket.socket(socket.AF_INET, sockets.SOCK_STREAM)
# Binding socket to the  address of the server
server_socket.bind(ADDR)


def handle_client(conn, addr):
    """ This function will  handle all the communication between the server and
    individual client. With use of threading module it will be possible to handle
    several clients in one process (each client in a separate thread). This function
    will run concurrently with the start() function.

    When a new connection to the server occurs, we will store the address of that
    connection (client's IP address and port) as addr and the socket object as conn
    param addr: client's address
    param addr: client's socket
    """
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    while connected:
        # This is a "blocking line of code" where the server will not pass any message
        # untill it recevies a message from the client.
        # HEADER argument determines the accepted max length of the coming message
        msg_length = conn.recv(HEADER).decode(FORMAT)
        msg_length = int(msg_length)
        # Receiving the actual message
        msg = conn.recv(msg_lengt).decode(FORMAT)
        if msg == DISCONNECT_MESSAGE:
            connected = False
        # Printing the received message and where it came from
        print(f"[{addr}] {msg}")
    # Close the connection
    conn.close()
