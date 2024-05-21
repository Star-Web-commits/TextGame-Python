#Otherside Picnic inspired game
from random import randint
from Character import Player, ForthKind

game_running = True
Menu = True
Play = True
game_results = []

#characters
Soarow = Player("Soarow", 150, 20, 30, Sane)
Toriko = Player("Toriko", 200, 40, 15, Sane)

#Enemies
# Kunekune
Kunekune = ForthKind("Kunekune", 1000, 20, Bored)

# Lady Hasshaku
Lady_Hasshaku = ForthKind("Lady Hasshaku", 12000, 30, Venegeful)


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

    

