import os
import json

from flask import Flask
from flask import request, render_template
from collections import deque

from calc_processing.config import settings
from calc_processing.calculations import calculate_with_process_pool_exec, opers
from calc_processing.db_methods import connect_to_db, add_data, get_data

app = Flask(__name__, template_folder="templates")
history = deque(maxlen=5)


@app.route("/", methods=['GET', 'POST'])
def start():
    return render_template('base.html')


@app.route("/operations")
def operations():
    return f'''{opers}'''


@app.route("/full_hist", methods=['GET', 'POST'])
def full_hist():

    form = render_template('history.html')

    if request.method == 'POST':
        oper = request.form.get('oper')
        limit = request.form.get('limit')
        offset = request.form.get('offset')
        my_query = get_data(session, oper, limit, offset)
        html_list = ''
        for res in my_query:
            str = f'{res.operator}, {res.number1}, {res.number2}, {res.result};'
            res_str = json.dumps(str, indent=0)
            html_list += f'<h4>{res_str}</h4>'
        return f'''{form}
{html_list}
'''

    return form


@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    # handle the POST request
    if request.method == 'POST':
        expr = request.form.get('expr')
        res, err = calculate_with_process_pool_exec(expr).split(':::')
        add_data(session, expr, float(res))

        oper_to_hist = expr + ' == ' + res
        history.appendleft(oper_to_hist)

        recent = '  <<>>  '.join(list(history))
        return render_template('calculator_post.html',
                                recent=recent,
                                res=res,
                                err=err)

    # otherwise handle the GET request
    return render_template('calculator_get.html')


if __name__ == "__main__":
    session = connect_to_db()
    app.run(host=settings.HOST,
            port=settings.HTTP_PORT)
