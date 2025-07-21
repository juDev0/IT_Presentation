import socket

server_socket = socket.socket()
server_socket.bind(("0.0.0.0", 12345))
server_socket.listen()

conn, addr = server_socket.accept()
print(f"Connected to {addr}")

while True:
    # Receive first
    msg = conn.recv(1024).decode()
    print(f"Friend: {msg}")

    # Then send
    message = input("You: ")
    conn.send(message.encode())
