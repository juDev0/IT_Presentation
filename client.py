import socket

import threading 

# create a socket
# the socket in which all the conversation will be nade possible
client_socket = socket.socket()

# connect to the sever
# it connects to the socket ot the other server with the port since its hostinhg
client_socket.connect(("192.168.88.24",12345)) 

# starts two threads
def receive():
    msg = client_socket.recv(1024).decode()
    print(f"Friend: {msg}")


def send():
    message = input()
    client_socket.send(message.encode())

# runs both threads 
threading.Thread(target=receive).start()
threading.Thread(target= send).start()