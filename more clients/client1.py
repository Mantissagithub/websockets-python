import socket

HEADERSIZE = 10

def client_task():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(), 12345))

    full_msg = ''
    new_msg = True
    while True:
        msg = s.recv(16)
        if new_msg:
            print(f"[Client 1] New message length: {msg[:HEADERSIZE].decode('utf-8')}")
            msglen = int(msg[:HEADERSIZE].decode('utf-8'))
            new_msg = False

        full_msg += msg.decode("utf-8")

        if len(full_msg) - HEADERSIZE == msglen:
            print(f"[Client 1] Full message received: {full_msg[HEADERSIZE:]}")
            break

if __name__ == "__main__":
    client_task()
