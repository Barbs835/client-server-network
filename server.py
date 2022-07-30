import socket
import threading
from cryptography.fernet import Fernet
import time
from itertools import repeat , chain

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
HEADER = 1024
crypt = Fernet('sqcyNL5kz2mxWb1KL2QSZWY-GCERE-scEgWBbvq9CCk=')
DISCONNECT_MESSAGE = "QUIT"
SEPARATOR = "<SEPARATOR>"

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
            client_conn, client_addr = server.accept()
            print(f"Client at {client_addr} has connected to server.")
            # Passing the new connection socket object and address to the handle_client function
            # Each clinet connection will be handled in a new thread
            thread = threading.Thread(target=handle_client, args=(client_conn, client_addr))
            thread.start()
            print("[STARTING] server is starting...")
            # Print the amount of client connections to the server (subtracting 1 as there is 1
            # active connection on the server that is always running and listening
            print(f"[ACTIVE CONNECTIONS] {threading.activeCount()-1}")
        except ConnectionAbortedError:
            print("An established connection was aborted by the software in your host machine")


def handle_client(client_conn, client_addr):
    connected = True
    while connected:
        msg = server.recv(HEADER).decode()
        if len(msg) == 0:
            return
        if msg == DISCONNECT_MESSAGE:
            print(f"[DISCONNECTING] from client {client_addr}")
            server.close()
            break
        else:
            try:
                # When clients sends file, the beginning of the streamed data will contain the
                # name of the file, the size and whether it is encrypted. Hence, servers should
                # extract this metadata first
                file_name, file_size, encryption =  data.split(SEPARATOR)
                filesize = int(file_size)
                # Creating empty bytearray object which will hold received data in bytes.
                received_data = bytearray()
                # Looping collection of the HEADER size packets of data sent from client
                while len(received_data) < file_size:
                    data_packet = socket.recv(HEADER)
                    received_data.extend(data_packet)

                print('\nFile received: ' + file_name)
                with open(filename, "wb") as f:
                    # Save the file in the same directory as the program
                    f.write(received_data)
                    f.close()
                    print('The file has been saved in the same directory folder')
                    # Print content to the screen
                    try:
                        # Decode the byte array data into a readable format
                        decoded_data = received_data.decode()
                        print('Printing the content on the screen:\n')
                        print(file_content_as_string)

                        if content_type.strip() == 'ENCRYPTED':
                            print('\nAttempting to decrypt encrypted data.')
                            try:
                                # Decrypt the file previously saved in
                                # received_files folder
                                # EncryptionHelper.decrypt_content(filename)
                                pass
                            except:
                                print('Unable to decrypt. THere might be an issue with the encryption key.')
                    except UnicodeDecodeError:
                        print('Code cannot decode byte.')
            except Exception as ex:
                print("Unable to read the data")


server_start()
handle_client()



