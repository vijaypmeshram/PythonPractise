#  " SNAKE WATER GUN GAME

print("Welcome to SNAKE WATER GUN GAME")

chance = 0
point = 0
computer = 0
user = 0

while (chance < 10):

    import random
    names = ["snake", "water", "gun"]
    comChoice = random.choice(names)
    """Above line select name from list randomly"""

    # now input taken from user
    print("Select one from snake, water, gun")
    userChoice = input()

    if comChoice == "snake" and userChoice == "water":
        def addPoint():
            global point
            point = point + 1
            print("Computer win")
            return  point
        addPoint()
        computer = point
        chance = chance + 1

    elif comChoice == "snake" and userChoice == "gun":
        def addPoint():
            global point
            point = point + 1
            print("user win")
            return  point
        addPoint()
        user = point
        chance = chance + 1

    elif comChoice == "water" and userChoice == "gun":
        def addPoint():
            global point
            point = point + 1
            print("Computer win")
            return  point
        addPoint()
        computer = point
        chance = chance + 1

    elif comChoice == "water" and userChoice == "snake":
        def addPoint():
            global point
            point = point + 1
            print("user win")
            return  point
        addPoint()
        user = point
        chance = chance + 1

    elif comChoice == "gun" and userChoice == "snake":
        def addPoint():
            global point
            point = point + 1
            print("Computer win")
            return  point
        addPoint()
        computer = point
        chance = chance + 1

    elif comChoice == "gun" and userChoice == "water":
        def addPoint():
            global point
            point = point + 1
            print("user win")
            return  point
        addPoint()
        user = point
        chance = chance + 1

    elif comChoice == "snake" and userChoice == "snake":
        print("round nullified, Try again")
        chance = chance + 1

    elif comChoice == "water" and userChoice == "water":
        print("round nullified, Try again")
        chance = chance + 1

    elif comChoice == "gun" and userChoice == "gun":
        print("round nullified, Try again")
        chance = chance + 1

    else:
        print(" check your input")

def compare():
    if computer > user :
        print(" computer won the game")
        print("computer win with", computer, "points")
    if computer < user :
        print(" user won the game")
        print("user win with", user, "points")
    elif computer == user :
        print(" this match is tie")
compare()
