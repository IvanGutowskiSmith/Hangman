wordToGuess = "theword"
guessesRemaining = 9

guessedLetter = input("Guess a letter\n")
if wordToGuess.__contains__(guessedLetter):
    print("Letter " + guessedLetter + " is correct")
else:
    guessesRemaining = guessesRemaining -1
    print("Sorry letter " + guessedLetter + " is incorrect")
    print("You have " + str(guessesRemaining) + " guesses remaining.")

