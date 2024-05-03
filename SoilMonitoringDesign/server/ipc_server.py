#!/usr/bin/env python3
# ipc_server.py

import socket
import statistics

HOST = socket.gethostbyname('ipc_server_dns_name')  # The server's hostname or IP address
PORT = 9898        # The port used by the server

def check_environment(temperature, humidity, pH, co2, light_intensity):
    # Check temperature
    temp_status = "Normal" if 20 <= temperature <= 25 else "Out of range"
    
    # Check humidity
    hum_status = "Normal" if 30 <= humidity <= 60 else "Out of range"
    
    # Check pH
    pH_status = "Normal" if 5.5 <= pH <= 7.5 else "Out of range"
    
    # Check CO2 concentration
    co2_status = "Normal" if co2 < 1000 else "High"
    
    # Check light intensity
    light_status = "Normal" if 300 <= light_intensity <= 500 else "Out of range"
    
    return f"Temperature: {temp_status}, Humidity: {hum_status}, pH: {pH_status}, CO2 Concentration: {co2_status}, Light Intensity: {light_status}"
    


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
            status = check_environment(data[0], data[1], data[2], data[3], data[4])
            conn.sendall(status.encode())
            print(status)
