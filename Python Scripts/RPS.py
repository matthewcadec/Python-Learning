from random import randint

t = ["Rock","Paper","Scissors"]

computer = t[randint(0,2)]
player = False

while player == False:
    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print("Computer has chosen", computer)
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("Computer has chosen", computer)
            print("You lose!", computer, "covers", player)
        else:
            print("Computer has chosen", computer)
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("Computer has chosen", computer)
            print("You lose!", computer, "cut", player)
        else:
            print("Computer has chosen", computer)
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("Computer has chosen", computer)
            print("You lose...", computer, "smashes", player)
        else:
            print("Computer has chosen", computer)
            print("You win!", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")

player = False
computer = t[randint(0,2)]

# We thank you for trying something new!