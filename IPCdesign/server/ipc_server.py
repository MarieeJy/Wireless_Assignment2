#!/usr/bin/env python3
# ipc_server.py

import socket
import statistics

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 9898        # Port to listen on (non-privileged ports are > 1023)

def process_data(data):
    numbers = list(map(float, data.decode().split()))
    mean = statistics.mean(numbers)
    median = statistics.median(numbers)
    stdev = statistics.stdev(numbers)
    return f"Mean: {mean}, Median: {median}, Standard Deviation: {stdev}"

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