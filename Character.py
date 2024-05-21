class Player:
    def stats(self, Name: str, Health:int, Attack: int, Heal: int, Status: str):
        self.Name = Name
        self.Health = Health
        self.Attack = Attack
        self.Heal = Heal
        self.Status = Status


    def status(self, Target, Anxious: bool, Scared: bool, Frozen: bool, Fear: bool, Angry: bool) -> str:
        self.Target = Target
        self.Anxious = Anxious
        self.Scared = Scared
        self.Frozen = Frozen
        self.Fear = Fear
        self.Angry = Angry
        pass

class ForthKind:
    def monsterStats(self, Name: str, Health: int, Attack: int, Status: str):
        self.Name = Name
        self.Health = Health
        self.Attack = Attack
        self.Status = Status

    def damage(self, ):
        pass
