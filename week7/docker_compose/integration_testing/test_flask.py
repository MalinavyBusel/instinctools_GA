import requests


def test_calculations_get():
    res = requests.get('http://flask_server:5000/calculator')
    assert res.status_code == 200


def test_calculations_post():
    res = requests.post('http://flask_server:5000/calculator', data={'expr': 'add 5 5'})
    result, _, _ = res.text.partition('. </h1>')
    _, _, num = result.partition(': ')
    assert num == '10.0'


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