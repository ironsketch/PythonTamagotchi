from Pet import Pet
import sys
import time

def playGame(thePet):
    choice = 1
    while(choice != 0):
        try:
            theTime = int(time.time())
            choice = int(input("What would you like to do?\n0 Quit, 1 Play, 2 Feed, 3 Water, 4 Punch, 5 Status: "))
            thePet.randomBehavior()
            if(choice == 0):
                sys.exit()
            if(choice == 1):
                thePet.play(25, 10)
            if(choice == 2):
                thePet.feed(20)
            if(choice == 3):
                thePet.water(20)
            if(choice == 4):
                thePet.punch(10)
            if(choice == 5):
                thePet.status()
            if(thePet.die(0)):
                print("You killed your pet... you monster!!! :(")
                main()
            if(thePet.ageUp(int(time.time()))):
                print("%s is now a year older! They are %d years old!" % (thePet.getName(), thePet.getAge()))
            thePet.happiness(-5)
            thePet.save(int(time.time()))
            print()

        except:
            print()

def newPet(petName):
    newPet = Pet(petName.replace(' ', '_'), 0, 50, 20, 20, 0, int(time.time()), int(time.time()))
    return newPet

def loadPet(petName):
    petInfo = open(petName.replace(' ', '_') + ".pet", 'r')
    petList = petInfo.read()
    petList = petList.split(' ')
    newPet = Pet(petList[0], int(petList[1]), int(petList[2]), int(petList[3]), int(petList[4]), int(petList[5]), int(petList[6]), int(petList[7]))
    newPet.whenYouWereGone(int(time.time()))
    playGame(newPet)

def main():
    try:
        choice = int(input("Would you like to load or create a new Pet? (1, 0) "))
        if(choice):
            petName = input("What is the name of your pet? ")
            loadPet(petName)
        else:
            petName = input("What will you name your new pet? ")
            playGame(newPet(petName))
    except:
        print("That was an invalid choice, did you spell your pet name wrong?")
        main()

if __name__ == "__main__":
    main()
