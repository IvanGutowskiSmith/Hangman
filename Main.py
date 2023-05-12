# Variables
wordToGuess = "because"
correctGuessedLetters = []
incorrectGuessedLetters = []
continueToGuess = True

# Logic functions

def printStatus():
    for letter in wordToGuess:
        if correctGuessedLetters.__contains__(letter):
            print(letter,end="")
        else:
            print("_ ",end="")
    
    print("\n\nIncorrect guesses: "+str(incorrectGuessedLetters))


def makeGuess():
    guessedLetter = input()
    if wordToGuess.__contains__(guessedLetter):
        correctGuessedLetters.append(guessedLetter)
    else:
        incorrectGuessedLetters.append(guessedLetter)


def continueGuessing():
    moreLettersToGuess = False
    for letter in wordToGuess:
        if letter not in correctGuessedLetters:
            moreLettersToGuess = True
    
    if moreLettersToGuess == True:
        continueToGuess = True
    else:
        print("Well done, all letters guessed")
        continueToGuess = False
        

# Main Loop

print("Welcome to hangman, please guess a letter\n")
printStatus()
continueGuessing()

while continueToGuess == True:
    makeGuess()
    printStatus()
    continueGuessing()