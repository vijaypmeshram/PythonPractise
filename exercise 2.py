print("GUESS MY NUMBER")
print("you have limited number of guess i.e 10")

g = 0

while ( g < 10 ):
    print("Enter your number between 10 to 50")
    num = int(input())
    g=g+1
    if g == 10:
        print("you are out of attempts")
        print("GAME OVER")
    elif num >= 27:
        print("tour number is more than my number")
        print("you attempt", g, "guesses")
    elif num <= 25:
        print("your number is less than my number")
        print("you attempt", g, "guesses")
    elif num == 26 :
        print("you won")
        print("you have completed game in ", g)
        break
