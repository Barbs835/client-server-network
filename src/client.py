
"""Client Side

Run this file to create, serialize and send a dictionary
and send a text file to the server.
"""

import socket
import pickle
import json

from dict2xml import dict2xml
from cryptography.fernet import Fernet
from os.path import exists as file_exists

# Key for fernet encryption
#crupt_key = "R29kemlsbGFJc0p1c3RBSHVnZVRvYWRDYWxsZWRUaW0="
client_crupt_key = "sqcyNL5kz2mxWb1KL2QSZWY-GCERE-scEgWBbvq9CCk="

default_dictionary = {}


# Functions for encryption of text
def encrypt(message: bytes):
    """Encrypt the provided variable

    Key arguments
    message -- the value to be encrypted
    Function annotation: message should be in byte format
    """
    return Fernet(client_crupt_key).encrypt(message)



# Parse user input to make sure correct
def user_input(choices):
    """Validate User Input
    Take user input and make sure
    it matches what the program is
    expecting

    Key Arguments
    choices -- Value the user inputs
    """
    found = "false"

    while found == "false":
        user_choice = input()
        if(user_choice.lower() in choices):
            return user_choice.lower()
        else:
            print("### Please choose a correct option ###")


def check_file():
    """Check file exists and filetype is correct"""
    found = "false"

    while found == "false":
        path = input()
        path_split = path.split(".")

        if(file_exists(path) is True):
            if(path_split[len(path_split) - 1] == "txt"):
                print("### File found ###")
                return path
        if(path_split[len(path_split) - 1] != "txt"):
            print("### Filetype is incorrect")
            print("### Please enter your filename ending in .txt ###")
        else:
            print("### File does not exist ###")
            print("### Please enter your filename ending in .txt ###")


# Send data to server
def send_data(serialized_data, PORT):
    """Send the data to the server

    Key arguments
    serialized_data -- a string of serialized data
    PORT -- Server port number eg. 5000
    """
    # getting HOST (which is the local machine) IP address
    HOST = socket.gethostbyname(socket.gethostname()) 

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(serialized_data.encode('latin1'))
        data = s.recv(1024)
        return "Data Sent"


def dictionary_enter():
    """Create a custom dictionary"""
    global default_dictionary
    value_amounts = ""
    value_amounts = input("### How many values do you want to use? ###\n")
    while not value_amounts.isnumeric():
        value_amounts = input("### Please enter a number ###\n")
    for v in range(int(value_amounts)):
        dict_key = input("### Enter a key ###\n")
        dict_value = input("### Enter a value ###\n")
        default_dictionary[dict_key] = dict_value


def serialize(default_dict, s_type):
    """Serialize data
    Key arguments:
    default_dict -- dictionary object to use as a default if other dictionary is not provided
    s_type -- type of serilisation required
    """
    serialized = ""
    method = ""
    if(s_type == '1'):
        serialized = pickle.dumps(default_dict)
        method = "pickle"
    if(s_type == '2'):
        serialized = json.dumps(
            default_dict, sort_keys=True, indent=4).encode()
        method = "json"
    if(s_type == '3'):
        serialized = dict2xml(default_dict, wrap='root', indent="").encode()
        method = "xml"
    return serialized, method


def parse_final_data(method, serialized, option):
    """Concatenate Optional Variables

    Key arguments
    method -- Serialization method: Pickle Binary (1), Json (2), XML (3)
    serialized -- the seralized data
    option -- Output method: Print to Screen (1) or Save to File (2)
    """
    return method + '~' + str(serialized)[2:-1] + '~' + str(option)


def main():
    """Client Main Function
    The starting point for execution for the programme.
    """
    global default_dictionary
    """Serialize Section"""

    print("### Serialization Section ###")
    # Dictionary to send
    print("### Do you wish to manually enter a dictionary? (Y) (N) ###")
    choices = ["y", "n"]
    d_type = user_input(choices)
    if(d_type == "y"):
        dictionary_enter()
    else:
        print("### Default Dictionary Used ###")
        default_dictionary = {"key1": "value1", "key2": "value2"}

    # Choose serialization type
    print("### Please Choose Serialization Type ###")
    print("### Pickle Binary (1), Json (2), XML (3) ###")
    choices = ["1", "2", "3"]
    s_type = user_input(choices)

    # Output to screen or file
    print("### Do you want to output to the",
          "screen (1) or file (2) ###")
    choices = ["1", "2"]
    option = user_input(choices)

    # Append to data for later review, seperated by ~
    # Method~Serialized~Print/File
    # e.g. json~{\n    "key1": "value1",\n    "key2": "value2"\n}~1

    serialized, method = serialize(default_dictionary, s_type)

    final_data = parse_final_data(method, serialized, option)

    # Send data to server
    send_data(final_data, 5050)
    print("### Your data has been sent ###")

    """File Section"""
    print("\n### File Section ###")
    # File choice and encrpytion
    print("### To send text file, please add it  to src directory first, then  enter file name ending in .txt here ###")

    file_choice = check_file()

    print("### Do you wish to locally encrypt your file? (Y) (N) ###")
    choices = ["y", "n"]
    enc_file_choice = user_input(choices)

    # Output to screen or file
    print("### Do you want to output the",
          "file to the screen (1) or file (2) ###")
    choices = ["1", "2"]
    option = user_input(choices)

    # Take in a read file
    f = open(file_choice, "r")
    file_contents = ""
    for line in f:
        file_contents += line

    # Encrypt file contents (.txt files only contain text)
    # Also adds user option at end if string
    # e.g: ENCRYPTEDCONTENTS~1
    enc_file_content = encrypt((file_contents + "~" + option).encode())

    # Save encrypted version to disc
    if(enc_file_choice == "y"):

        # Create encrypted file name XXXX_enc.txt
        # Changes forward slashes to backslashes
        file_choice = file_choice.replace("/", "\\")
        # Split on backslash
        file_choice = file_choice.split("\\")
        # Take last object from list
        file_choice = file_choice[len(file_choice) - 1]
        # Split on . to take just filename, no extension
        split_name = file_choice.split(".")
        enc_file_name = split_name[0] + "_enc.txt"

        # Create file
        file = open(enc_file_name, 'w')
        file.write(enc_file_content.decode())
        file.close()
        print(f"{enc_file_name} created!")

    send_data(enc_file_content.decode(), 5050)

if __name__ == "__main__":
    main()
