from flask import Flask, request
import random
import traceback

app = Flask(__name__)

secret = 0  # Holds secret number

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
    global secret
    secret = pickSecretNumber()
    return GUESS_HTML.format('')

@app.route("/guess")
def guess():
    try:
        theGuess = int(request.args['guess'])
        result = checkGuess(theGuess, secret)
    except ValueError:
        traceback.print_exc()
        return GUESS_HTML.format("Please enter a valid number")
    except Exception as e:
        traceback.print_exc()
        return GUESS_HTML.format("Oops! Something weird happened. Please contact the webmaster for help.")

    if theGuess == secret:
        return """You got it!"""
    else:
        return GUESS_HTML.format(result)
    
GUESS_HTML = """
<html>
<body>
<h1>Welcome to Guess</h1>

I've picked a secret number from 1 to 10.

<form action="/guess">
Enter your guess: <input type="text" name="guess">
<input type="submit" value="Guess">
</form>

{}

</body>
</html>
"""


if __name__ == "__main__":
    app.run(host='localhost', debug=True)
    
