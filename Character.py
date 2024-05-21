class Player:
    def __init__(self, Name: str, Health:int, Attack: int, Heal: int, Status: str):
        self.Name = Name
        self.Health = Health
        self.Attack = Attack
        self.Heal = Heal
        self.Status = Status

    def stats(self) -> str:
        return (f"Name: {self.Name}, Health: {self.Health}, Attack: {self.Attack}"
                f"Heal: {self.Heal}, Status: {self.status}")

    def status(self, Target, Anxious: str, Scared: str, Frozen: str, Angry: str, Sane: str) -> str:
        self.Target = Target
        self.Anxious = Anxious
        self.Scared = Scared
        self.Frozen = Frozen
        self.Angry = Angry
        self.Sane = Sane
        status_conditions = {
            'Anxious': self.Anxious,
            'Scared': self.Scared,
            'Frozen': self.Frozen,
            'Fear': self.Fear,
            'Angry': self.Angry,
            'Sane': self.Sane
        }
        active_conditions = [conditions for conditions, active in status_conditions.items() if active]
        return f"Target: {self.Target}, Status Conditions: {', '.join(active_conditions) if active_conditions else 'Sane'}"

    # def debuff(self) -> bool: I want this to just be like a simple true or false about the status, but I don't think it's necessary
    #     pass 

    def damage(self) -> int:
        Damage = self.damage
        if self.Anxious or self.Scared:
            Damage = int(Damage * 0.8)
        if self.Angry:
            Damage = int(Damage * 1.2)
        
        return Damage

    def healing(self) -> int:
        Healing_amount = self.Heal
        if self.Frozen:
            Healing_amount = int(Healing_amount * 0.5)
        if self.Sane:
            Healing_amount = int(Healing_amount * 1.2)

    


class ForthKind:
    def monsterStats(self, Name: str, Health: int, Attack: int, Status: str):
        self.Name = Name
        self.Health = Health
        self.Attack = Attack
        self.Status = Status

    def damage(self) -> int:
        pass

    def Status(self) ->str: #agitated, Scary, Hurt, Bored, Vengeful
        pass
