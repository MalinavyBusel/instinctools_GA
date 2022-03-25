import socket
import os

from calc_processing.calculations import calculate
from dotenv import load_dotenv


load_dotenv()
host, port = os.environ.get('HOST_AND_PORT').split(':')
HOST = str(host)
PORT = int(port)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            data = conn.recv(1024).decode(encoding='utf-8')
            if not data:
                break
            send_data = calculate(data).encode(encoding='utf-8')
            conn.sendall(send_data)

