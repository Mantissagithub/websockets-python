import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET - IPv4, SCOCK_STREAM - TCP
s.connect((socket.gethostname(),1234))

msg = s.recv(1024)
print(msg.decode("utf-8"))
