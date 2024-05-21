#Otherside Picnic inspired game
from random import randint
from Character import Player, ForthKind

game_running = True
Menu = True

game_results = []

#Player
Soarow = Player("Name")

Toriko = Player()


#Enemies
# Kunekune
Kunekune = ForthKind()



# Lady Hasshaku
Lady_Hasshaku = ForthKind()


# Main game Loop
while game_running:
    while Menu:
        print("1, NEW GAME")
        print("2, LOAD GAME")
        print("3, RULES")
        print("4, QUIT GAME")

        Choice = input("What is your decision? #")

        if Choice == "1":
            #clear() #this will clear any other save file
            pass
            #the players characters are to be inisalised here
            # I'll also add in a file so there can be a save state to pick up and put down the game

        elif Choice == "2":
            #this will load the save file that was made in the previous round of gaming
            pass

        elif Choice == "3":
            pass

        elif Choice == "4":
            pass

