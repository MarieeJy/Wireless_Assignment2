#!/usr/bin/env python3
# ipc_server.py

import socket
import statistics

HOST = socket.gethostbyname('ipc_server_dns_name')  # The server's hostname or IP address
PORT = 9898        # The port used by the server

def process_data(data):
    numbers = list(map(float, data.decode().split()))
    mean = statistics.mean(numbers)
    median = statistics.median(numbers)
    stdev = statistics.stdev(numbers)
    return f"Mean: {mean:.2f}, \nMedian: {median:.2f}, \nStandard Deviation: {stdev:.2f}"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            result = process_data(data)
            conn.sendall(result.encode())
            print('Data:', data)
            print(result)