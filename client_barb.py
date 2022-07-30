import socket
import pickle
import json
import sys
from dict2xml import dict2xml
from cryptography.fernet import Fernet



# Setting up Server IP address and port constants
PORT = 5050
# if server is not a local host, replace with IP address string
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "QUIT"
HEADER = 1024
crypt = Fernet('sqcyNL5kz2mxWb1KL2QSZWY-GCERE-scEgWBbvq9CCk=')
dictionary = {}
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SEPARATOR = "<SEPARATOR>"


def connect_to_server():
    try:
        # Connecting to the server
        client_socket.connect(ADDR)
        print('[CONNECTED]')
        return True
    except ConnectionRefusedError:
        print(f"No connection could be made. Check if there is a server running at IP, Port: {ADDR}")
        return False


def client_disconnect():
    """
    Client closes successful connection.
    """
    if client_socket is not None:
        client_socket.send(f"CLIENT HAS DISCONNECTED".encode())
        client_socket.close()
        print("Client has disconnected")

def convert_dictionary_object(format):
  """ Serialize the dictionary to JSON, XML, BINARY
  """
  if format == "BINARY":
    with open('dictionary_object.bin', 'wb') as f:
      pickle.dump(dictionary, f)
      print('Dictionary serialised as BINARY. Filename: dictionary_object.bin')
  elif format == "JSON":
    with open('dictionary_object.json', 'w') as f:
      json.dump(dictionary, f)
      print('Dictionary serialised as JSON. Filename: dictionary_object.json')
  elif format == "XML":
    xml_content = dict2xml(dictionary, wrap="dictionary", indent="  ")
    with open('dictionary_object.xml', 'w') as f:
      f.write(xml_content)
      f.close()
      print('Dictionary serialised as XML. Filename: dictionary_object.xml')

def send_file_to_server(file_name, encryption):
        """ sned the file that contains either dictionary or text (if text, it could be
        encrypted). Dictionary object is saved to either XML, JSON or BINary file

        """
        if encryption == True:
            content_mode = "ENCRYPTED"
            file_name = EncryptionHelper.encrypt_content(filename)
            messageEncode = message.encode()
            messageEncrypt = crypt.encrypt(messageEncode)
            print("Message has been encrypted")
        else:
            content_mode = "NOT_ENCRYPTED"

        # get the size of the file we want to send
        file_size = os.path.getsize(filename)

        client_socket.send(f"{file_name}{SEPARATOR}{file_size}{SEPARATOR}{content_mode}".encode())
        # start sending the file
        with open(file_name, "rb") as file:
          while True:
            bytes_read = file.read(HEADER)
            if not bytes_read:
              # transfer is done. nothing left to be sent
              break
              # Send what has been read so far
              client_socket.sendall(bytes_read)
              print(filename + ' was successfully sent to the server.')

if __name__ == "__main__":
    if connect_to_server():
        # display command line prompt for client to key in a command
        command = input("From the list of the available commands:\
        \nhelp\nadd_dictionary\nadd_text\nQUIT\n type one of the commands")
        while cmd != DISCONNECT_MESSAGE:
            if command.lower() == "help":
                # Show help menu
                help_menu()
            elif command.lower() == "add_dictionary":
                pass
        # TO DO ........................
        # command line ask user to either add text entry or dictionary entry
         # if users chooses text entry:
        #ask if text should be encrypted or not, then save it as a file and transfer to server
        # if user choses dictionary entry
        # ask what format to serialise it to (JSON XML BINARY) then save it as a file and
        # send it to the server