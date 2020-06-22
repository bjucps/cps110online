from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return HTML_FORM

HTML_FORM = """
<html><body>
    <form action="/hello">
        Enter your username: <input type="text" name="username" value="Hello"><br>
        Enter your age: <input type="text" name="age" value="18"><br>
        <input type="submit" value="Click here for a friendly greeting">
    </form>
</body></html>
"""

@app.route('/hello')
def hello():
    username = request.args.get('username', 'World')
    age = request.args.get('age', '15')

    return HELLO_HTML.format(username, age)

HELLO_HTML = """
    <html><body>
    <h1>Hello, {0}!</h1>
    You are {1} years old.
    </body></html>
"""

if __name__ == "__main__":
    app.run(host='localhost', debug=True)

