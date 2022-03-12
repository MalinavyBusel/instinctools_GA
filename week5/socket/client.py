import socket
import os

from dotenv import load_dotenv


load_dotenv()
host, port = os.environ.get('HOST_AND_PORT').split(':')
HOST = str(host)
PORT = int(port)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    expr = input('Enter the expression: ')
    s.sendall(expr.encode(encoding='utf-8'))
    if expr:
        data = s.recv(1024).decode(encoding='utf-8')
        res, _, error = data.partition(':::')
        if res:
            print(f"Received {res}")
        elif error:
            print(error)
            print(res)
        else:
            print('Something unexpected happened. Please, connect with'
                  'the support service.')
            print(res)
    else:
        print('Session ended.')
