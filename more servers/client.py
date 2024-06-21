import socket
import threading

HEADERSIZE = 10

def client_task(server_address, server_port, client_id):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server_address, server_port))  # Connect to the specified server

    full_msg = ''
    new_msg = True
    while True:
        msg = s.recv(16)
        if new_msg:
            print(f"[Client {client_id}] New message length: {msg[:HEADERSIZE].decode('utf-8')}")
            msglen = int(msg[:HEADERSIZE].decode('utf-8'))
            new_msg = False

        full_msg += msg.decode("utf-8")

        if len(full_msg) - HEADERSIZE == msglen:
            print(f"[Client {client_id}] Full message received: {full_msg[HEADERSIZE:]}")
            break

if __name__ == "__main__":
    server_details = [
        ('localhost', 12345, 'Server 1'),
        ('localhost', 12346, 'Server 2')
    ]

    client_threads = []

    for address, port, id in server_details:
        t = threading.Thread(target=client_task, args=(address, port, id))
        t.start()
        client_threads.append(t)

    for t in client_threads:
        t.join()
