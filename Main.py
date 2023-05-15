import requests
import xml.etree.ElementTree as ET

## Variables
wordToGuess = ""
correctGuessedLetters = []
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
        print("finding word....." + str(fleschScore))

        # > 50 = easy
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

print("Welcome to hangman, please type your dificuilty level: Easy(1) - Hard (2)\n")
wordToGuess = getRandomWord(input())
print(wordToGuess)

printStatus()
continueGuessing()

while continueToGuess == True:
    makeGuess()
    printStatus()
    continueGuessing()

exit()