import socket
import threading
from cryptography.fernet import Fernet
import time


PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
HEADER = 1024
crypt = Fernet('sqcyNL5kz2mxWb1KL2QSZWY-GCERE-scEgWBbvq9CCk=')


def server_start():
    """Set socket and start server to listen for connections"""
    server = socket.socket()
    server.bind(ADDR)
    server.listen()
    print(f"[SERVER IS LISTENING] on {SERVER} ")
    connected = True
    while connected:
        try:
            # This line of code blocks the process by waiting for new connection to the server
            # When connection occurs server stores the client's "conn" socket object and
            # connection address
            client_socket, client_addr = server.accept()
            print(f"Client at {client_addr} has connected to server.")
            # Passing the new connection socket object and address to the handle_client function
            # Each clinet connection will be handled in a new thread
            thread = threading.Thread(target=handle_client, args=(client_socket, client_addr))
            thread.start()
            print("[STARTING] server is starting...")
            # Print the amount of client connections to the server (subtracting 1 as there is 1
            # active connection on the server that is always running and listening
            print(f"[ACTIVE CONNECTIONS] {threading.activeCount()-1}")
        except ConnectionAbortedError:
            print("An established connection was aborted by the software in your host machine")


def handle_client(client_socket, client_addr):
    connected = True
    while connected:
        msg = server.recv(HEADER).decode()
        if len(msg) == 0:
            return
        if msg == 'EXIT':
            print('Closing connection with client at: %s' % (address,))
            # Freeing the socket
            server.close()
            break



server_start()
handle_client()



