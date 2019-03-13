import random

words = ["apple", "butter", "cat", "dog", "elephant", "future", "ghost", "history", "icing", "jump", "kill", "little", "moth", "naughty", "octopus", "peanut", "quit", "race", "simple", "terrible", "unbeatable", "very", "wild", "xenoblast", "yoda", "zap"]

def wordChange(word, xs):
    hidden = word
    for i in range(len(xs)):
        hidden = hidden.replace(xs[i], '_')
    return hidden

def hangman():
    choice = random.randint(0, len(words) - 1)
    word = words[choice]
    hidden = '_' * len(word)
    hide = []
    hide.append(word[random.randint(0, len(word) - 1)])
    hide.append(word[random.randint(0, len(word) - 1)])
    hide.append(word[random.randint(0, len(word) - 1)])
    hidden = wordChange(word, hide)
    print(word)
    print(hidden)


hangman()
