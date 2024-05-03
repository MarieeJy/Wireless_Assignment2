#!/usr/bin/env python3
# ipc_client.py

import socket
import random

HOST = socket.gethostbyname('ipc_server_dns_name')  # The server's hostname or IP address
PORT = 9898        # The port used by the server

numbers = ' '.join(str(random.randint(1, 100)) for _ in range(50))   # generate a random number for testing

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(numbers.encode())
    data = s.recv(1024)

print('Data:', numbers)
print(data.decode())