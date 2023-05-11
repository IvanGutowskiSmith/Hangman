wordToGuess = "theword"

guessedLetter = input("Guess a letter\n")
if wordToGuess.__contains__(guessedLetter):
    print("Letter " + guessedLetter + " is correct")
else:
    print("Sorry letter " + guessedLetter + " is incorrect")