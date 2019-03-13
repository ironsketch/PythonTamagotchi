import random

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

    def play(self, game, exp):
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

    def ageUp(self, time):
        if(time - self.time > 86400):
            self.age += int(time / self.time)
            self.time = time
            return True
        return False

    def happiness(self, amount):
        if(self.happy <= 0):
            self.happy = 0
            self.die(5)
        else:
            self.happy += amount

    def save(self):
        saveFile = open(self.name + ".pet", 'w')
        saveFile.write(
                self.name + " " + str(self.age) + " " +
                str(self.hunger) + " " + str(self.thirst) + " " +
                str(self.happy) + " " + str(self.death) + " " +
                str(self.time))
        saveFile.close

    def randomBehavior(self):
        rInt = random.randint(0, 100)
        if(rInt == 4):
            print(self.name + " made a huge mess and trashed your home! Their happiness went up!")
            self.happy += 5
        if(rInt == 44):
            print(self.name + " fell down a well. They are fine now but they got hurt!")
            self.die(5)
        if(rInt == 94):
            print(self.name + " found a crusty cheetoh and ate it.")
            self.feed(2)

    def status(self):
        print("%s\nAge: %d, Hunger: %d, Thirst: %d, Happiness: %d, Death: %d" % (self.name, self.age, self.hunger, self.thirst, self.happy, self.death))
