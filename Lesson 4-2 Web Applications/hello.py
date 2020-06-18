from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    current_datetime = datetime.now()
    return HOME_HTML.format(current_datetime)

HOME_HTML = """<html><body>
    <h1>Hello, world!</h1>
    The time is {}.
    <a href="/page2">Click here</a> for page 2.
    </body></html>
"""

@app.route('/page2')
def page2():
    return """<html><body>Here is page 2.</body></html>"""

@app.route('/hello')
def hello():
    name = request.args.get('name', 'World')
    age = request.args.get('age', '15')

    return HELLO_HTML.format(name, age)

HELLO_HTML = """<html><body>
    <h1>Hello, {}!</h1>
    You are {} years old.</body></html>
"""


if __name__ == "__main__":
    app.run(host='localhost', debug=True)

