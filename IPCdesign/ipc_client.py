#!/usr/bin/env python3
# ipc_client.py

import socket
import random

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 9898        # The port used by the server

numbers = ' '.join(str(random.random() * 100) for _ in range(50))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(numbers.encode())
    data = s.recv(1024)

print('Received', data.decode())