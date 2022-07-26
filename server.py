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
DISCONNECT_MESSAGE = "DISCONNECT"

# Creating a new socket (AF_INET argument  determines  family of # addresses that this
# socket can  communicate with (in this case, Internet Protocol v4 addresses).
# SOCK_STREAM is a transmission mechanism (in this case, two-way byte streams of data).
# Anything that connects to the specified IP & port now, will hit that socket.
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Binding socket to the  address of the server
server.bind(ADDR)


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
        # If message length is not none
        if msg_length:
            msg_length = int(msg_length)
            # Receiving the actual message
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            # Printing the received message and where it came from
            print(f"[{addr}] {msg}")
    # Close the connection
    conn.close()

def start():
    """Starts the socket and allows our server to start listening for connections & then
    handling those connections by passing them to handle_client(conn, addr) function which
    will run in a new thread.
    """
    server.listen()
    print(f"[SERVER IS LISTENING] Server is listening on {SERVER}")
    # Server will continue to listen while it is not turned off/ crashed etc.
    while True:
        # This line of code blocks the process by waiting for new connection to the server
        # When connection occurs server stores the "conn" socket object and connection address
        conn, addr = server.accept()
        # Passing the new connection socket object and address to the handle_client function
        # Each clinet connection will be handled in a new thread
        # target is the collable object
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        # Print the amount of client connections to the server (subtracting 1 as there is 1
        # active connection on the server that is always running and listening
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount()-1}")

print("[STARTING] server is starting...")
start()
