import socket

# Create the socket
client_socket = socket.socket()

# Connect to the server (replace with your server's IP and port)
client_socket.connect(("192.168.137.1", 12345))

print("Connected to server. You can now start chatting!")

while True:
    # Send message to the server
    message = input("You: ")
    client_socket.send(message.encode())

     # Receive message from the server
    msg = client_socket.recv(1024).decode()
    print(f"Friend: {msg}")
    