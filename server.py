# this creates a socket for communication
import socket

# this helps to show the message in a thread form
import threading

# start listening for connections
server_socket = socket.socket()

# it the host and also, the port for chattin
server_socket.bind(("0.0.0.0",12345))  # 0.0.0.0 = any IP, that this Pc has.

# starts listening for connections / searching for connections
server_socket.listen()

# Accept connection
conn, addr = server_socket.accept()
print(f"connected to {addr}")

# starting the threads
# recives and send at the same time
def receive():
    while True:
        # the recv is you receving from this client_socket 
        msg = conn.recv(1024).decode()  # the 1024 bytes at a time in reciving the data
       # e.g 1 byte is = 1 latter e.g "Happy" = 5 bytes making it like a space for the data to recive
        print(f"Friend:{msg}")

def send():
    while True:
        message = input()
        conn.send(message.encode())

# This runs both threads
threading.Thread(target= receive).start()
threading.Thread(target= send).start()