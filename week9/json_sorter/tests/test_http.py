import requests


unsorted_1 = {'sequence': [73, 65, -1, 843, 9.9, 23, 1, 45, 11.11]}
unsorted_2 = {'sequence': [23, 354, 11, 245, 363.1, -3949, 363, 3496]}
unsorted_3 = {'sequence': [6354, 754, 897, 1, -45, -588, -3.3, 890, 0]}
unsorted_4= {'sequence': [-85, -7, 0, 2, 4365, -8675436474, -74347, -10, 95, 3]}
unsorted_5= {'sequence': [4.0, 236.236, 753.1, 0.1, 25, 25.001, 175, 109, 55.555]}
unsorted_6 = {'sequence': [1, 2144, 31, 4, 5]}

sorted_1 = [-1, 1, 9.9, 11.11, 23, 45, 65, 73, 843]
sorted_2 = [23, 354, 11, 245, 363.1, -3949, 363, 3496]
sorted_3 = [-588, -45, -3.3, 0, 1, 754, 890, 897, 6354]
sorted_4 = [-8675436474, -74347, -85, -10, -7, 0, 2, 3, 95, 4365]
sorted_5 = [0.1, 4.0, 25, 25.001, 55.555, 109, 175, 236.236, 753.1]


def test_http_get():
    res = requests.get('http://http:5000/api/v0.1/posted-sequence')
    assert res.status_code == 200


def test_http_post_1():
    post_res = requests.post('http://http:5000/api/v0.1/posted-sequence', json=unsorted_1)
    assert post_res.json()['sorted_sequence'] == sorted_1


def test_http_post_2():
    post_res = requests.post('http://http:5000/api/v0.1/posted-sequence', json=unsorted_2)
    assert post_res.json()['sorted_sequence'] == sorted_2


def test_http_post_3():
    post_res = requests.post('http://http:5000/api/v0.1/posted-sequence', json=unsorted_3)
    assert post_res.json()['sorted_sequence'] == sorted_3


def test_http_post_4():
    post_res = requests.post('http://http:5000/api/v0.1/posted-sequence', json=unsorted_4)
    assert post_res.json()['sorted_sequence'] == sorted_4


def test_http_post_5():
    post_res = requests.post('http://http:5000/api/v0.1/posted-sequence', json=unsorted_5)
    assert post_res.json()['sorted_sequence'] == sorted_5


def test_http_post_6():
    post_res = requests.post('http://http:5000/api/v0.1/posted-sequence', json=unsorted_6)
    assert post_res.json()['time_taken']
