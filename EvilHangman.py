import random

def getDictionary():
    dictionary = []

    with open("/usr/share/dict/words") as openfileobject:
        for line in openfileobject:
            if line[:-1].isalpha():
                dictionary.append(line[:-1])
    return dictionary

def makeFamilies(biggestFamily, guess):
    families = {}
    for word in biggestFamily:
        pattern = []
        for index, letter in enumerate(word):
            if letter == guess:
                pattern.append(index)
        pattern = tuple(pattern)
        if(pattern in families):
            families[pattern].append(word)
        else:
            families[pattern] = [word]
    return families

def reduceFamilies(families):
    biggestFamily = []
    for family in families.values():
        if len(family) > len(biggestFamily):
            biggestFamily = family

    for word in biggestFamily:
        print word
        
    return biggestFamily

def showProgress(guesses, word):
    progress = ""
    for letter in word:
        if letter in guesses:
            progress = progress +  letter
        else:
            progress = progress + " _"
    print progress

def handleTurn(biggestFamily, guesses, chances):
    print "What's your guess?"
    guess = raw_input().lower()

    while not (guess.isalpha() and len(guess) == 1):
        print "That is not an APPROPRIATE GUESS."
        print "Please guess again."
        guess = raw_input().lower()

    if guess in guesses:
        print "LOL you already guessed that."
        chances = chances - 1
    else:
        guesses.append(guess)
        biggestFamily = reduceFamilies(makeFamilies(biggestFamily, guess))
        if guess not in biggestFamily[0]:
            chances = chances - 1
        showProgress(guesses, biggestFamily[0])
    return (biggestFamily, chances)

def checkForWin(word, guesses):
    for letter in word:
        if letter not in guesses:
            return False
    return True

#Game Starts Here#

chances = 8

numLetters = random.randint(5, 10)

dictionary = filter(lambda word : len(word) == numLetters, getDictionary())

for word in dictionary:
    print word

guesses = []

while chances > 0:
    (dictionary, chances) = handleTurn(dictionary, guesses, chances)
    if checkForWin(dictionary[0], guesses):
        print "You win. The word is " + dictionary[0]

print "Game over."
