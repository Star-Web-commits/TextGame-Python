class Player:
    def __init__(self, Name: str, Health:int, Attack: int, Heal: int, Status: str):
        self.Name = Name
        self.Health = Health
        self.Attack = Attack
        self.Heal = Heal
        self.Status = Status


    def status(self, Target) -> None:
        self.Target = Target
        pass

class ForthKind:
    def __init__(self, Name: str, Health: int, Attack: int, Status: str):
        self.Name = Name
        self.Health = Health
        self.Attack = Attack
        self.Status = Status
