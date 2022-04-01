import requests


def test_calculations_get():
    res = requests.get('http://flask_server:5000/calculator')
    assert res.status_code == 200


def test_calculations_post_0():
    res = requests.post('http://flask_server:5000/calculator', data={'expr': 'add 5 5'})
    result, _, _ = res.text.partition('. </h1>')
    _, _, num = result.partition(': ')
    assert num == '10.0'


def test_calculations_post_1():
    res = requests.post('http://flask_server:5000/calculator', data={'expr': 'truediv 10 6'})
    result, _, _ = res.text.partition('. </h1>')
    _, _, num = result.partition(': ')
    assert num == '1.67'


def test_calculations_post_2():
    res = requests.post('http://flask_server:5000/calculator', data={'expr': 'sub 10 6'})
    result, _, _ = res.text.partition('. </h1>')
    _, _, num = result.partition(': ')
    assert num == '4'


def test_calculations_post_3():
    res = requests.post('http://flask_server:5000/calculator', data={'expr': 'mul 5 5'})
    result, _, _ = res.text.partition('. </h1>')
    _, _, num = result.partition(': ')
    assert num == '60'


def test_calculations_post_4():
    res = requests.post('http://flask_server:5000/calculator', data={'expr': 'floordiv 5 5'})
    result, _, _ = res.text.partition('. </h1>')
    _, _, num = result.partition(': ')
    assert num == '1'


def test_calculations_post_5():
    res = requests.post('http://flask_server:5000/calculator', data={'expr': 'gt 1 5'})
    result, _, _ = res.text.partition('. </h1>')
    _, _, num = result.partition(': ')
    assert num == '0'


def test_calculations_post_6():
    res = requests.post('http://flask_server:5000/calculator', data={'expr': 'hypot 3 4'})
    result, _, _ = res.text.partition('. </h1>')
    _, _, num = result.partition(': ')
    assert num == '5.0'


def test_calculations_post_7():
    res = requests.post('http://flask_server:5000/calculator', data={'expr': 'eq 5 5'})
    result, _, _ = res.text.partition('. </h1>')
    _, _, num = result.partition(': ')
    assert num == '1'


def test_calculations_post_8():
    res = requests.post('http://flask_server:5000/calculator', data={'expr': 'rshift 3 4'})
    result, _, _ = res.text.partition('. </h1>')
    _, _, num = result.partition(': ')
    assert num == '0'


def test_main():
    res = requests.get('http://flask_server:5000/')
    assert res.status_code == 200, 'Something is wrong with flask app. The server is unavailable.'


def test_history_get():
    res = requests.get('http://flask_server:5000/full_hist')
    assert res.status_code == 200


def test_history_post():
    res1 = requests.post('http://flask_server:5000/full_hist', data={'oper': 'truediv'})
    assert res1.status_code == 200
    res2 = requests.post('http://flask_server:5000/full_hist', data={'oper': 'add',
                                                                     'offset': '1',
                                                                     'limit': '1'})
    assert res2.status_code == 200
    res3 = requests.post('http://flask_server:5000/full_hist')
    assert res3.status_code == 200