from flask import Flask, request
import traceback

app = Flask(__name__)

@app.route('/')
def home():
    return HTML_FORM.format('', '', '')

HTML_FORM = """
    <form action="/hello">
        Enter your username: <input type="text" name="username" value="{}"><br>
        Enter your age: <input type="text" name="age" value="{}"><br>
        <input type="submit" value="Click here for a friendly greeting">
        {}
    </form>
"""

@app.route('/hello')
def hello():
    username = request.args.get('username', '')
    age = request.args.get('age', '')

    if username == '':
        return HTML_FORM.format(username, age, 'Please enter a username.')
    
    try:
        age = int(request.args['age'])
    except Exception as e:
        traceback.print_exc()
        return HTML_FORM.format(username, age, 'Please enter a valid age.')

    return HELLO_HTML.format(username, age)

HELLO_HTML = """
    <html><body>
    <h1>Hello, {0}!</h1>
    You are {1} years old.
    </body></html>
"""

if __name__ == "__main__":
    app.run(host='localhost', debug=True)

