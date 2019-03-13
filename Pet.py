import random

class Pet:
    def __init__(self, name, age, happy, hunger, thirst, death, time, timeHours):
        self.name = name
        self.age = age
        self.happy = happy
        self.hunger = hunger
        self.thirst = thirst
        self.death = death
        self.dead = False
        self.time = time
        self.timeHours = timeHours

    def die(self, ouch):
        self.death += ouch
        if(self.death >= 100):
            return True
        return False

    def feed(self, food):
        self.hunger += food
        if(self.hunger < 0):
            self.hunger = 0
            self.die(10)
        if(self.hunger > 100):
            self.hunger = 100

    def water(self, water):
        self.thirst += water
        if(self.thirst < 0):
            self.thirst = 0
            self.die(10)
        if(self.thirst > 100):
            self.thirst = 100

    def game1(self):
        rInt = random.randint(0, 10)
        guess = int(input(self.name + " is thinking of a number between 0 and 10. What is it? "))
        if(guess == rInt):
            print("You guessed right!")
            return True
        print("Nope!")
        return False

    def wordChange(self, word, xs):
        hidden = word
        for i in range(len(xs)):
            hidden = hidden.replace(xs[i], '_')
        return hidden

    def game2(self):
        words = ["apple", "butter", "cat", "dog", "elephant", "future", "ghost", "history", "icing", "jump", "kill", "little", "moth", "naughty", "octopus", "peanut", "quit", "race", "simple", "terrible", "unbeatable", "very", "wild", "xenoblast", "yoda", "zap"]
        choice = random.randint(0, len(words) - 1)
        word = words[choice]
        hidden = '_' * len(word)
        hide = []
        for i in range(3):
            letter = word[random.randint(0, len(word) - 1)]
            if(letter not in hide):
                hide.append(letter)
        hidden = self.wordChange(word, hide)
        letters = []
        attempts = 6
        while(attempts > 0):
            guess = input("Make a letter guess! %s You have %d guesses remaining! " % (hidden, attempts))
            if(guess in hide):
                hide.remove(guess)
                hidden = self.wordChange(word, hide)
            else:
                letters.append(guess)
                attempts -= 1
            print("So far you have incorrectly guessed")
            print(letters)
            if(not hide):
                print("Great job! %s" % (word))
                return True

        print("You failed! And should be ashamed... %s " % (word))
        return False

    def play(self, game, exp):
        print()
        choice = int(input("Game 1 or 2? "))
        won = False
        if(choice == 1):
            won = self.game1()
        if(choice == 2):
            won = self.game2()
        if(won):
            if(self.happy + game > 100):
                self.happy = 100
            else:
                self.happy += game
            if(self.hunger <= 0 or self.thirst <= 0):
                self.die(5)
            self.feed(-exp)
            self.water(-exp)

    def punch(self, hit):
        if(not self.die(hit)):
            if(self.happy <= 0):
                self.happy = 0
                self.die(hit)

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def whenYouWereGone(self, time):
        timePassed = int((time - self.timeHours) / 3600)
        self.feed(-timePassed)
        self.water(-timePassed)
        self.happiness(-timePassed)

    def ageUp(self, time):
        if(time - self.time > 86400):
            self.age += int((time - self.time) / 86400)
            self.time = time
            return True
        return False

    def happiness(self, amount):
        if(self.happy <= 0):
            self.happy = 0
            self.die(5)
        else:
            self.happy += amount

    def save(self, time):
        saveFile = open(self.name + ".pet", 'w')
        saveFile.write(
                self.name + " " + str(self.age) + " " +
                str(self.hunger) + " " + str(self.thirst) + " " +
                str(self.happy) + " " + str(self.death) + " " +
                str(self.time) + " " + str(time))
        saveFile.close

    def randomBehavior(self):
        rInt = random.randint(0, 75)
        if(rInt == 4):
            print(self.name + " made a huge mess and trashed your home! Their happiness went up!")
            self.happy += 5
        if(rInt == 13):
            print("Someone picked on " + self.name + " and they cried ALL FREAKIN DAY...")
            self.happy -= 5
        if(rInt == 23):
            print(self.name + " fell down a well. They are fine now but they got hurt!")
            self.die(5)
        if(rInt == 24):
            print(self.name + " Found a pretty shell on the ground. They picked it up and then got pooped on by a crow. " + self.name + " then kept walking, feeling sad but found a 20$ bill! They decided to buy candy with it. After eating TOO much candy they threw up all over your couch.")
            self.die(5)
        if(rInt == 44):
            print(self.name + " found a crusty cheetoh and ate it.")
            self.feed(2)

    def status(self):
        print("%s\nAge: %d, Hunger: %d, Thirst: %d, Happiness: %d, Death: %d" % (self.name, self.age, self.hunger, self.thirst, self.happy, self.death))
