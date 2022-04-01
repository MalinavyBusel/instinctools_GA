import json

from flask import Flask
from flask import request
from collections import deque

from calc_processing.config import settings
from calc_processing.calculations import calculate, opers
from calc_processing.db_methods import connect_to_db, add_data, get_data

app = Flask(__name__)
history = deque(maxlen=5)


@app.route("/", methods=['GET', 'POST'])
def start():
    return '''<a href="calculator">Calculator</a>
<a href="operations">Operations</a>
<a href="full_hist">Full_History</a>'''


@app.route("/operations")
def operations():
    return f'''{opers}'''


@app.route("/full_hist", methods=['GET', 'POST'])
def full_hist():

    form = '''
               <form method="POST">
                   <div><label>Operator: <input type="text" name="oper"></label></div>
                   <div><label>Limit: <input type="text" name="limit"></label></div>
                   <div><label>Offset: <input type="text" name="offset"></label></div>
                   <input type="submit" value="Find">
               </form>
               <a href="operations">Operations</a>
               <a href="calculator">Calculator</a>'''

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
    form = '''
           <form method="POST">
               <div><label>Expression: <input type="text" name="expr"></label></div>
               <input type="submit" value="Solve">
           </form>
           <a href="operations">Operations</a>
           <a href="full_hist">Full_History</a>'''

    # handle the POST request
    if request.method == 'POST':
        expr = request.form.get('expr')
        res, err = calculate(expr).split(':::')
        add_data(session, expr, float(res))

        oper_to_hist = expr + ' == ' + res
        history.appendleft(oper_to_hist)

        recent = '  <<>>  '.join(list(history))
        return f'''<h1>The result is: {res}. {err}</h1>\n 
{form}
<h4>History:{recent}<h4>'''

    # otherwise handle the GET request
    return form


if __name__ == "__main__":
    session = connect_to_db()
    app.run(host=settings.HOST,
            port=settings.PORT)
