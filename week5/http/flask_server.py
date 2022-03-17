from flask import Flask
from flask import request, redirect, url_for
from instinctools_GA.week5.calculations import calculate, opers
from collections import deque
app = Flask(__name__)

history = deque(maxlen=5)


@app.route("/", methods=['GET', 'POST'])
def start():
    return '''<a href="calculator">Calculator</a>
<a href="operations">Operations</a>'''


@app.route("/operations")
def operations():
    return f'''{opers}'''


@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    form = '''
           <form method="POST">
               <div><label>Expression: <input type="text" name="expr"></label></div>
               <input type="submit" value="Solve">
           </form>
           <a href="operations">Operations</a>'''

    # handle the POST request
    if request.method == 'POST':
        expr = request.form.get('expr')
        res, err = calculate(expr).split(':::')

        oper_to_hist = expr + ' == ' + res
        history.appendleft(oper_to_hist)

        recent = '  <<>>  '.join(list(history))
        return f'''<h1>The result is: {res}. {err}</h1>\n 
{form}
<h4>History:{recent}<h4>'''

    # otherwise handle the GET request
    return form


if __name__ == "__main__":
    app.run()
