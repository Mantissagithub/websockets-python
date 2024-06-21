import socket

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET - IPv4, SOCK_STREAM - TCP
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Reuse the address
s.bind((socket.gethostname(), 12345))  # Use port 12345
s.listen(5)  # Queue of 5 connections

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established")

    msg = "Welcome to the server!"
    msg = f'{len(msg):<{HEADERSIZE}}' + msg

    clientsocket.send(bytes(msg, "utf-8"))
    clientsocket.close()
