# Material from  lecturecast week 6

# -------------streams + socket packages----------------


"""
The sockets package allows low-level access to network communications. Sockets are supported by the operating system and allows you to implement clients and servers for both connection-oriented and connectionless protocols.


https://www.tutorialspoint.com/python_network_programming/python_sockets_programming.htm

demonstration shows the two-way communication abilities of sockets:
"""
# -------------stream.py --------------------
import asyncio

async def tcp_echo_client(message):
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 8888)
    print(f'Send: {message}')
    writer.write(message.encode())
    await writer.drain()

    data = await reader.read(100)
    #print(f"Received: {data.decode()}")

    print('Close the connection')
    writer.close()
    await writer.wait_closed()

asyncio.run(tcp_echo_client('Hello World!'))



# -------------stream-server.py --------------------


import asyncio

async def handle_echo(reader, writer):
    data = await reader.read(100)
    message = data.decode()
    addr = writer.get_extra_info('peername')

    print(f"Received {message!r} from {addr!r}")

    print(f"Send: {message!r}")
    writer.write(data)
    await writer.drain()

    print("Close the connection")
    writer.close()

async def main():
    server = await asyncio.start_server(
        handle_echo, '127.0.0.1', 8888)

    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')

    async with server:
        await server.serve_forever()

asyncio.run(main())



#  ----------------Serialsiation---------------------



import pickle
test_variable = 10
file_handler = open(“test.pck”,”wb”)
pickle.dump(test_variable, file_handler)



"""
Pickle Function

The pickle package comes with many functions other than dump.

Dump → write stream to file

Dumps → returns a bytes object in pickle format of the variable

Load → load pickle file into variable

Loads → loads byte object from dump as a variable
"""



# ------------ exception handling --------------------------

# Source: https://www.tutorialspoint.com/the-try-finally-clause-in-python


try:
   fh = open("testfile", "r")
   try:
      fh.write("This is my test file for exception handling!!")
   finally:
      print ("Going to close the file")
      fh.close()
except IOError:
   print ("Error: can't find file or read data”)


# -------- encryption    string--------------------------

"""
https://www.geeksforgeeks.org/how-to-encrypt-and-decrypt-strings-in-python/
"""

#    ! pip install cryptography



from cryptography.fernet import Fernet

# we will be encryting the below string.
message = "hello geeks"

# generate a key for encryptio and decryption
# You can use fernet to generate
# the key or use random key generator
# here I'm using fernet to generate key

key = Fernet.generate_key()

# Instance the Fernet class with the key

fernet = Fernet(key)

# then use the Fernet class instance
# to encrypt the string string must must
# be encoded to byte string before encryption
encMessage = fernet.encrypt(message.encode())

print("original string: ", message)
print("encrypted string: ", encMessage)

# decrypt the encrypted string with the
# Fernet instance of the key,
# that was used for encrypting the string
# encoded byte string is returned by decrypt method,
# so decode it to string with decode methos
decMessage = fernet.decrypt(encMessage).decode()

print("decrypted string: ", decMessage)


# ---------- encryption file ---------------------

#  https://pypi.org/project/securefile/
