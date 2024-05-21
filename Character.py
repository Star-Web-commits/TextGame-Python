class Player:
    def stats(self, Name: str, Health:int, Attack: int, Heal: int, Status: str):
        self.Name = Name
        self.Health = Health
        self.Attack = Attack
        self.Heal = Heal
        self.Status = Status

    def status(self, Target, Anxious: str, Scared: str, Frozen: str, Fear: str, Angry: str, Sane: str) -> str:
        self.Target = Target
        self.Anxious = Anxious
        self.Scared = Scared
        self.Frozen = Frozen
        self.Fear = Fear
        self.Angry = Angry
        self.Sane = Sane

    def debuff(self) -> bool:
        pass

    def damage(self) -> int:
        pass

    def Healing(self) -> int:
        pass

    


class ForthKind:
    def monsterStats(self, Name: str, Health: int, Attack: int, Status: str):
        self.Name = Name
        self.Health = Health
        self.Attack = Attack
        self.Status = Status

    def damage(self) -> int:
        pass

    def Status(self) ->str: #agitated, Scary, Hurt, Bored, Venegeful
        pass
