import random
a = ("kamen'", "nognici", "bymaga")
playerChoose= -1
computerChoose = -1

def guess():
    global playerChoose, computerChoose
    while ((playerChoose < 0 or playerChoose > 2) or (playerChoose == computerChoose)) :
        if(playerChoose == computerChoose and playerChoose > -1 and playerChoose < 3):
            print("player choose: ", a[playerChoose], " computer choose: ", a[computerChoose], "\n reroll...")
        playerChoose = int(input("Choose one:\n1) kamen' 2) nognici 3) bymaga\n")) - 1
        computerChoose = random.randint(0,2)

guess()

print("computer choose: " + a[computerChoose])

if((playerChoose == 0 and computerChoose == 1) or(playerChoose == 1 and computerChoose == 2 )or(playerChoose == 2 and computerChoose == 0 ) ):
    print("player won")

else:
    print("computer won")
