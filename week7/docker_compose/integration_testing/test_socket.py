import socket


s = socket.socket()
address = 'socket_server'
port = 65432


def test_socket_connection():
    result = 1
    try:
        s.connect((address, port))
    except Exception as e:
        result = 0
        error = f"something's wrong with {address}:{port}. Exception is {e}"
    assert result, error


def test_socket_calculating():
    try:
        expr = 'add 3 3'
        s.sendall(expr.encode(encoding='utf-8'))
        data = s.recv(1024).decode(encoding='utf-8')
        res, _, error = data.partition(':::')
    finally:
        s.close()
    assert res == '6.0'
