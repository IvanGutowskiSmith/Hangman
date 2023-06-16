import requests
import xml.etree.ElementTree as ET
import tkinter as tk

## Variables
wordToGuess = ""
correctGuessedLetters = []
correctGuessedLettersUiString = ""
incorrectGuessedLetters = []
continueToGuess = True

# Logic functions
def getRandomWord(desiredDificuilty):
    withinRange = False
    while withinRange == False:
        # Obtain random word
        response_API = requests.get('https://random-word-api.herokuapp.com/word?length=5')
        wordToGuess = response_API.text.strip("[\"\"]")

        readabilityScore = requests.post('https://datayze.com/callback/readability', data={'txt': wordToGuess})
        root = ET.fromstring(readabilityScore.text)
        fleschScore = float(root.find('.//scores').attrib['flesch'])
        print("finding word... FleschScore: " + str(fleschScore))

        # >= 50 = easy
        # < 50 = hard
        withinRange = False
        match desiredDificuilty:
            case "1":
                if fleschScore >= 50:
                    withinRange = True
                    break
            case "2":
                if fleschScore < 50:
                    withinRange = True
                    break
            case _:
                print("Enter value between 1 and 2")
                break
        
    return wordToGuess


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

def printStatus():
    correctGuessedLettersUiString = ""
    for letter in wordToGuess:
        if correctGuessedLetters.__contains__(letter):
            correctGuessedLettersUiString.__add__(letter,end="")
        else:
            print("_ ",end="")
    return correctGuessedLettersUiString
    print("\n\nIncorrect guesses: "+str(incorrectGuessedLetters))
    updateGUI ()    


class GUI:
    #Initialize elements once, then update them later. But in same method to avoid global variable use
    def __init__(self):
        self.window = tk.Tk()
        self.titleLabel = tk.Label(text="HANGMAN GAME")
        self.titleLabel.pack()

        self.incorrectGuessesUiLabel = tk.Label(self.window, text="Incorrect Guesses []")
        self.incorrectGuessesUiLabel.pack()

        self.correctGuessesUiLabel = tk.Label(self.window, text="Word to Guess Here" )
        self.correctGuessesUiLabel.pack()
    
    def updateIncorrectGuessesUiLabel(self, incorrectGuessedLetters):
        self.correctGuessesUiLabel.config(text="Incorrect Guesses: "+ str(incorrectGuessedLetters))

    def updateCorrectGuessesUiLabel(self, correctGuessesUiLabel):
        self.correctGuessesUiLabel.config(text=str())


def loadUI():
    window = tk.Tk()
    titleLabel = tk.Label(text="HANGMAN GAME")
    titleLabel.pack()

    incorrectGuessesUILabel = tk.Label(text="Incorrect Guesses: " + str(incorrectGuessedLetters))
    incorrectGuessesUILabel.pack()


def updateGUI():

    incorrectGuessesUILabel.config(text="Incorrect Guesses: " + str(incorrectGuessedLetters))


    #incorrectGuessesUILabel = tk.Label(text="Incorrect Guesses: " + str(incorrectGuessedLetters))
    #incorrectGuessesUILabel.pack()
    #window.update()

    #window.mainloop()



# Main Loop

print("Welcome to hangman, please type your dificuilty level: Easy(1) - Hard (2)\n")
wordToGuess = getRandomWord(input())
print(wordToGuess)
loadUI()



printStatus()
continueGuessing()

while continueToGuess == True:
    makeGuess()
    printStatus()
    continueGuessing()

exit()