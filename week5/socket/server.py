import socket
import os

from dotenv import load_dotenv
from operator import *


load_dotenv()
host, port = os.environ.get('HOST_AND_PORT').split(':')
HOST = str(host)
PORT = int(port)

oper_dict = {'sum': add, 'div': truediv, 'diff': sub,
             'mult': mul, 'expon': pow, 'floordiv': floordiv,
             'and': and_, 'xor': xor, 'or': or_,
             'is': is_, 'is_not': is_not, 'lshift': lshift,
             'mod': mod, 'rshift': rshift, 'lt': lt, 'le': le,
             'eq': eq, 'ne': ne, 'gt': gt, 'ge': ge}


def calculate(expression: str):
    try:
        oper, val1, val2 = expression.strip().split(' ')
        res = oper_dict[oper](float(val1), float(val2))
        return str(res) + ':::'
    except ZeroDivisionError:
        return ':::You are trying to divide by zero.'
    except KeyError:
        return ':::There is no such operation.'
    except ValueError:
        return ':::Invalid arguments or their types.'


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

