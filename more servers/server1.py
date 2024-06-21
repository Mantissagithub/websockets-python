import socket

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET - IPv4, SOCK_STREAM - TCP
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Reuse the address
s.bind(('localhost', 12345))  # Use 'localhost' and port 12345
s.listen(5)  # Queue of 5 connections

print("Server 1 is listening on port 12345...")

while True:
    clientsocket, address = s.accept()
    print(f"Server 1: Connection from {address} has been established")

    msg = "Welcome to Server 1!"
    msg = f'{len(msg):<{HEADERSIZE}}' + msg

    clientsocket.send(bytes(msg, "utf-8"))
    clientsocket.close()
