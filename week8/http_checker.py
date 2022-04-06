import requests
import threading
import concurrent.futures as cf
import json

from flask import Flask
from flask import request
from typing import Callable
from requests.exceptions import ConnectionError


### business logic
def status_getter(url: str, res_dict: dict):
    try:
        res = requests.head(url).status_code
        if res == 405:
            res = requests.get(url).status_code
        if res != 200:
            value_str = 'invalid'
        else:
            value_str = 'positive_res'
    except ConnectionError:
        value_str = 'invalid'
    with lock:
        res_dict[value_str].append(url)
    return None


def http_checker(urls: list) -> dict:
    executor = cf.ThreadPoolExecutor()
    futures = []
    health_dict = {'positive_res': [], 'invalid': []}
    for url in urls:
        futures.append(executor.submit(status_getter, url, health_dict))
    done, not_done = cf.wait(futures, return_when=cf.ALL_COMPLETED)
    executor.shutdown()
    return health_dict


### HTTP logic
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def calculator():
    form = '''
           <form method="post">
<p><textarea id="healthcheck" name="urls_list" rows="4" cols="50"></textarea>
<input type="submit" value="Отправить"></p>'''
# Не создавал папку teplates, т.к. использую только 1 небольшой шаблон
    # handle the POST request
    if request.method == 'POST':
        urls_list_unparsed = request.form.get('urls_list')
        urls_list = urls_list_unparsed.split(', ')
        health_res = json.dumps(http_checker(urls_list))
        return f'''{form}
<h5>{health_res}</h5>\n 
'''

    # handle the GET request
    return form


lock = threading.Lock()
app.run()