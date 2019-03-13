import random

words = ["apple", "butter", "cat", "dog", "elephant", "future", "ghost", "history", "icing", "jump", "kill", "little", "moth", "naughty", "octopus", "peanut", "quit", "race", "simple", "terrible", "unbeatable", "very", "wild", "xenoblast", "yoda", "zap"]

def wordChange(word, xs):
    hidden = word
    for i in range(len(xs)):
        hidden = hidden.replace(xs[i], '_')
    return hidden

def game2():
    choice = random.randint(0, len(words) - 1)
    word = words[choice]
    hidden = '_' * len(word)
    hide = []
    hide.append(word[random.randint(0, len(word) - 1)])
    hide.append(word[random.randint(0, len(word) - 1)])
    hide.append(word[random.randint(0, len(word) - 1)])
    hidden = wordChange(word, hide)
    attempts = 6
    while(attempts > 0):
        guess = input("Make a letter guess! %s You have %d guesses remaining! " % (hidden, attempts))
        if(guess in hide):
            print("The guess was %s and the length is %d" % (guess, len(guess)))
            hide.remove(guess)
            hidden = wordChange(word, hide)
            print(hide)
        else:
            attempts -= 1
        if(not hide):
            print("Great job! %s" % (word))
            return True
    print("You failed! And should be ashamed... %s " % (word))
    return False

game2()
