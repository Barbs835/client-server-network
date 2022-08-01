
""" Server Side
Run this file to open the server.
The server could process TXT , JSON, XML ,and files
The server and the clients should work at the same machine
This file created by Group C: Amr Ibrahim, Barbara Surowiecka, and Chun Wong
"""

import socket
import pickle
import json
import sys
import xmltodict

# from dict2xml import dict2xml
from cryptography.fernet import Fernet
from os.path import exists as file_exists

# Key for fernet encryption
#crupt_key = "R29kemlsbGFJc0p1c3RBSHVnZVRvYWRDYWxsZWRUaW0="
server_crupt_key = "sqcyNL5kz2mxWb1KL2QSZWY-GCERE-scEgWBbvq9CCk="

""" Data from socket """
in_data = ""

#Function for decrpytion of dictionary
def decrypt(token: bytes):
    """decryption of text based on the symmetric KEY"""
    try:
        return Fernet(server_crupt_key).decrypt(token)
    except (cryptography.fernet.InvalidToken, TypeError):
        print("The token is invalid")

# Starting the server at the defined port
def start_server(PORT):
    """Start up server

    Keyword arguments:
    PORT -- the desired port number eg. 5000 or 5050
    """
    global in_data
    #getting host IP address
    HOST = socket.gethostbyname(socket.gethostname())
    time_out = 900       # The waiting time to receive input

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.bind((HOST, PORT))
        except:
            print(f"Unable to bind to {HOST}:{PORT}")   # show the connection details to the user
            sys.exit(1)
        print(f"Server Open on {HOST}:{PORT}")
        print("The server is ready to process data ...")
        s.listen()                                      # Start to listen
        s.settimeout(time_out)
        conn, addr = s.accept()
        with conn:
            print(f"{addr[0]} Connected")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)
                in_data = repr(data)


# Function to read the serialized data
def serialized_receive():
    """Receiving Serialized data"""

    # Open server at port 5000
    start_server(5050)
    full_data = in_data[2:-1].split('~')

    # Parse received data
    message = full_data[1].replace('\\\\', '\\')
    message = message.encode('utf-8')
    message = message.decode('unicode-escape').encode('latin1')

    # De-serialize data based on the data types
    if (full_data[0] == "pickle"):
        dict_ = pickle.loads(message)
    if (full_data[0] == "json"):
        dict_ = json.loads(message)
    if (full_data[0] == "xml"):
        dict_ = xml_deserialize(message)

    # Output to screen or save to file
    if (full_data[2] == "1"):
        print(f"You provided the server with:\n{dict_}")
    if (full_data[2] == "2"):
        file_creator(str(dict_), "dictionary")


# Function to process XML
def xml_deserialize(message):
    """De-Serialize a Serialized XML string

    Keyword arguments:
    message -- the string to de-serialize
    """
    msg_parsed = str(message)[2:-1]
    msg_deserial = xmltodict.parse(msg_parsed)
    s_dict = msg_deserial["root"]
    try:
        s_dict.pop('#text')
        msg_dict = dict(s_dict)

        return(msg_dict)
    except KeyError:
        return(s_dict)


def file_receive():
    """Receiving File"""

    # Open server
    start_server(5050)

    full_data = in_data[2:-1]
    plain_text = decrypt(full_data.encode('utf-8')).decode()
    decrypt_text = plain_text.split("~")

    if(decrypt_text[1] == "1"):
        print(decrypt_text[0])
    if(decrypt_text[1] == "2"):
        file_creator(decrypt_text[0], "file")

# Support function to create file
def file_creator(content, type):
    """Create file

    Keyword arguments:
    content -- content for the file as a string
    """

    file_num = 1
    while(True):
        filename = type + str(file_num) + ".txt"
        # If file exists don't write, increment number
        if(file_exists(filename) is False):
            file = open(filename, 'w+')
            file.write(content)
            file.close()
            print(f"{filename} created!")
            return True

        file_num += 1

# The server main function
def main():
    """ Server Main Function
    The starting point for execution for the programme.
    """
    global in_data
    # Data from socket
    in_data = ""

    # For testing serialized_receive()
    if len(sys.argv) > 1:
        if(sys.argv[1] == "-T"):
            for i in range(2):
                serialized_receive()
    else:
        serialized_receive()
        file_receive()


if __name__ == "__main__":
    main()
