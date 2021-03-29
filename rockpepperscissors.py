from random import randint   #import random module
t = ["Rock", "Paper", "Scissors"]    #creating an array for RPS
comp = t[randint(0, 2)]    #random array memory for RPS
edwin = False   
while edwin == False:
    edwin = input("Rock, Paper, Scissors?")
    if edwin == comp:
        print("Tie!")
    elif edwin == "Rock":
        if comp == "Paper":
            print("You lose!", comp, "covers", edwin)
        else:
            print("You win!", edwin, "smashes", comp)
    elif edwin == "Paper":
        if comp == "Scissors":
            print("You lose!", comp, "cut", edwin)
        else:
            print("You win!", edwin, "covers", comp)
    elif edwin == "Scissors":
        if comp == "Rock":
            print("You lose...", comp, "smashes", edwin)
        else:
            print("You win!", edwin, "cut", comp)
    else:
        print("Check your spelling!")
    edwin = False
    comp = t[randint(0, 2)]
