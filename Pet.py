class Pet:
    def __init__(self, name, age, happy, hunger, thirst, death, time):
        self.name = name
        self.age = age
        self.happy = happy
        self.hunger = hunger
        self.thirst = thirst
        self.death = death
        self.dead = False
        self.time = time

    def die(self, ouch):
        self.death += ouch
        if(self.death > 100):
            return True
        return False

    def feed(self, food):
        self.hunger += food
        if(self.hunger < 0):
            self.hunger = 0
            self.die(10)

    def water(self, water):
        self.thirst += water
        if(self.thirst < 0):
            self.thirst = 0
            self.die(10)

    def play(self, game, exp):
        if(not self.die(exp)):
            if(self.happy + game > 100):
                self.game = 100
            else:
                self.happy += game
            self.feed(-exp)
            self.water(-exp)

    def punch(self, hit):
        if(not self.die(hit)):
            self.die(hit)

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def ageUp(self, time):
        if(self.time - time > 86,400):
            self.age += int(time / self.time)
            self.time = time

    def save(self):
        saveFile = open(self.name + ".pet", 'w')
        saveFile.write(
                self.name + " " + str(self.age) + " " +
                str(self.hunger) + " " + str(self.thirst) + " " +
                str(self.happy) + " " + str(self.death) + " " +
                str(self.time))
        saveFile.close

    def status(self):
        print("%s\nAge: %d, Hunger: %d, Thirst: %d, Happiness: %d, Death: %d" % (self.name, self.age, self.hunger, self.thirst, self.happy, self.death))
