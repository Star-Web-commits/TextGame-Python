#Otherside Picnic inspired game
from random import randint

game_running = True
game_results = []
#Central hub(Contains: HP, Attack and heal??? )
class Player:
    def __init__(self, Name: str, Health:int, Attack: int, Heal: int, Status: str):
        self.Name = Name
        self.Health = Health
        self.Attack = Attack
        self.Heal = Heal
        self.Status = Status

class ForthKind:
    def __init__(self, Name: str, Health: int, Attack: int, Status: str):
        self.Name = Name
        self.Health = Health
        self.Attack = Attack
        self.Status = Status


#Enemies
# Kunekune
Kunekune = ForthKind()



# Lady Hasshaku

# 

