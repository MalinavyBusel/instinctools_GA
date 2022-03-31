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


def test_socket_calculating_1():
    expr = 'add 0 0'
    s.sendall(expr.encode(encoding='utf-8'))
    data = s.recv(1024).decode(encoding='utf-8')
    res, _, error = data.partition(':::')
    assert res == '0'


def test_socket_calculating_2():
    expr = 'ne 1 1.0'
    s.sendall(expr.encode(encoding='utf-8'))
    data = s.recv(1024).decode(encoding='utf-8')
    res, _, error = data.partition(':::')
    assert res == '1'


def test_socket_calculating_3():
    expr = 'is 1 1'
    s.sendall(expr.encode(encoding='utf-8'))
    data = s.recv(1024).decode(encoding='utf-8')
    res, _, error = data.partition(':::')
    assert res == '1'


def test_socket_calculating_4():
    expr = 'atan2 3 5'
    s.sendall(expr.encode(encoding='utf-8'))
    data = s.recv(1024).decode(encoding='utf-8')
    res, _, error = data.partition(':::')
    assert res == '0.54'


s.close()
