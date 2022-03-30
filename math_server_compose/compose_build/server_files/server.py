import socket

from calc_processing.config import settings
from calc_processing.calculations import calculate
from calc_processing.db_methods import connect_to_db, add_data

HOST = settings.HOST
PORT = int(settings.S_PORT)

session = connect_to_db()

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
            res_data = calculate(data)
            res, _, err = res_data.split(':::')
            res = float(res) if res else float('nan')
            add_data(session, data, res)
            send_data = res_data.encode(encoding='utf-8')
            conn.sendall(send_data)

