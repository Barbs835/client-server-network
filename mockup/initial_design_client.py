import socket


# Setting up Server IP address and port constants
PORT = 5050
SERVER = "192.168.0.44"
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
HEADER = 1024


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



def connect_to_server():
    try:
        # Connecting to the server
        client.connect(ADDR)
        print('[CONNECTED]')
        return True
    except ConnectionRefusedError:
        print(f"No connection could be made. Check if there is a server running at IP, Port: {ADDR}")
        return False


def send_txt_file(txt_file):
    """
    reads the txt_file saved in the same directory as the client.py program and
    sends it to the server.
    :param txt_file_name: name and extention of the file for example "letter.txt"
    :return: True if file is sent and False otherwise
    """
    with open(txt_file, 'rb') as file_to_send:
        for data in file_to_send:
            client.sendall(data)
    print('end')
    client.close()



connect_to_server()
send_txt_file('toSend.txt')
