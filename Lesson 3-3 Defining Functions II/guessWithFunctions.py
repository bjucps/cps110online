import random

def pickSecretNumber():
    return random.randrange(1, 11)

def checkGuess(guess, secretNum):
    if guess < secretNum:
        print("Your guess is too low.")
    elif guess > secretNum:
        print("Your guess is too high.")
    else:
        print("You got it!!")
 
# main program
def main():
    secretNum = pickSecretNumber()

    numGuesses = 0
    guess = 0
    while guess != secretNum:

        guess = int(input("Enter your guess: "))
        numGuesses += 1
        checkGuess(guess, secretNum)

    print("It took you", numGuesses, "guesses.") 

main()  # execute main program
