# webguess2.py
#
# This version of webguess uses a hidden input field to store the
# secret number, so that multiple people can play the game
# at the same time.

from flask import Flask, request
import random
import traceback

app = Flask(__name__)

def pickSecretNumber():
    """Returns random number between 1 and 10"""    
    return random.randrange(1, 11)

def checkGuess(guess, secretNum):
    """Prints a hint showing relation of `guess` to `secretNum`"""    
    if guess < secretNum:
        return "Your guess is too low."
    elif guess > secretNum:
        return "Your guess is too high."
    else:
        return "You got it!!"
    

@app.route("/")
def start():
    secret = pickSecretNumber()
    print('Picked secret number:', secret)
    return GUESS_HTML.format(secret, '')

@app.route("/guess")
def guess():
    try:
        secret = int(request.args['secret'])
        theGuess = int(request.args['guess'])
        result = checkGuess(theGuess, secret)
    except ValueError:
        traceback.print_exc()
        return GUESS_HTML.format(secret, "Please enter a valid number")
    except Exception as e:
        traceback.print_exc()
        return GUESS_HTML.format(secret, "Oops! Something weird happened. Please contact the webmaster for help.")

    if theGuess == secret:
        return WIN_HTML
    else:
        return GUESS_HTML.format(secret, result)
    
GUESS_HTML = """
<html>
<body>
<h1>Welcome to Guess</h1>

I've picked a secret number from 1 to 10.

<form action="/guess">
Enter your guess: <input type="text" name="guess">
<input type="submit" value="Guess">
<input type="hidden" name="secret" value="{}">
</form>

{}

</body>
</html>
"""

WIN_HTML = """
<html>
<body>
<h1>You got it!</h1>
<a href="/">Play again</a>
"""


if __name__ == "__main__":
    app.run(host='localhost', debug=True)
    
