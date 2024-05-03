#!/usr/bin/env python3
# ipc_client.py

import socket
import random
import struct

HOST = socket.gethostbyname('ipc_server_dns_name')  # The server's hostname or IP address
PORT = 9898        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    while True:
        # geneate the value
        temperature = random.randint(10, 50)
        humidity = random.randint(0, 100)
        pH = random.randint(0, 14)
        CO2 = random.randint(400, 2000)
        light = random.randint(0, 100)

        # package the sensor values
        sensor_values = struct.pack('!5i', temperature, humidity, pH, CO2, light)

        # send values
        s.sendall(sensor_values)

        # get response
        data = s.recv(1024)

        # print the result
        print(f"Sent: temperature={temperature}℃, humidity={humidity}%, pH={pH}, CO2={CO2}ppm, light={light}%")
        print("Received:", data.decode())


