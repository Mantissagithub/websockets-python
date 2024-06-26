import socket

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET - IPv4, SCOCK_STREAM - TCP
s.connect((socket.gethostname(),1234))

full_msg = ' '
new_msg = True
while True:
    msg = s.recv(16)
    if new_msg:
        print(f"new message length: {msg[:HEADERSIZE].decode('utf-8')}")
        msglen = int(msg[:HEADERSIZE].decode('utf-8'))
        new_msg = False
        
    full_msg += msg.decode("utf-8")

    if len(full_msg)-HEADERSIZE == msglen:
        print("full msg recvd")
        print(full_msg[:HEADERSIZE])
        new_msg = True
        full_msg = ''

