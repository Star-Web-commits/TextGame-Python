from enum import Enum, auto

class Status(Enum):
    ANXIOUS = auto()
    SCARED = auto()
    FROZEN = auto()
    ANGRY = auto()
    SANE = auto()
    AGITATED = auto()
    SCARY = auto()
    INJURED = auto()
    BORED = auto()
    VENGEFUL = auto()


class Player:
    def __init__(self, Name: str, Health:int, Attack: int, Heal: int, Status: Status):
        self.Name = Name
        self.Health = Health
        self.Attack = Attack
        self.Heal = Heal
        self.Status = Status
        self.status_conditions = {
            Status.ANXIOUS: False,
            Status.SCARED: False,
            Status.FROZEN: False,
            Status.FEAR: False,
            Status.ANGRY: False,
            Status.SANE: True
        }

    def stats(self) -> str:
        return (f"Name: {self.Name}, Health: {self.Health}, Attack: {self.Attack}"
                f"Heal: {self.Heal}, Status: {self.status}")

    
    def set_status(self, condition: Status, value: bool):
        if condition in self.status_conditions:
            self.status_conditions[condition] = value

    
    def status(self) -> str:
        active_conditions = [condition.name for condition, active in self.status_conditions.items() if active]
        return f"Active Status Conditions: {', '.join(active_conditions) if active_conditions else 'None'}"
    
    
    def set_status(self, condition: Status, value: bool):
        if condition in self.status_conditions:
            self.status_conditions[condition] = value

    # def debuff(self) -> bool: I want this to just be like a simple true or false about the status, but I don't think it's necessary
    #     pass 

    def damage(self) -> int:
        # Example logic: calculate damage based on attack and status conditions
        damage = self.Attack
        if self.status_conditions[Status.ANXIOUS] or self.status_conditions[Status.SCARED]:
            damage = int(damage * 0.8)  # reduce damage by 20% if Anxious or Scared
        if self.status_conditions[Status.ANGRY]:
            damage = int(damage * 1.2)  # increase damage by 20% if Angry
        return damage

    def healing(self) -> int:
        # Example logic: calculate healing based on heal attribute and status conditions
        healing_amount = self.Heal
        if self.status_conditions[Status.FROZEN]:
            healing_amount = int(healing_amount * 0.5)  # reduce healing by 50% if Frozen
        if self.status_conditions[Status.SANE]:
            healing_amount = int(healing_amount * 1.2)  # increase healing by 20% if Sane
        return healing_amount

    


class ForthKind:
    def __init__(self, Name: str, Health: int, Attack: int, Status: Status):
        self.Name = Name
        self.Health = Health
        self.Attack = Attack
        self.Status = Status
        self.status_conditions = {
            Status.AGITATED: False,
            Status.SCARY: False,
            Status.INJURED: False,
            Status.BORED: False,
            Status.VENGEFUL: False

        }

    def stats(self) -> str:
        return (f"Name: {self.Name}, Health: {self.Health}, Attack: {self.Attack}"
                f"Status: {self.status}")



    def damage(self) -> int:
        Damage = self.damage
        if self.status_conditions[Status.BORED] or self.status_conditions[Status.SCARY]:
            Damage = int(Damage * 0.8)
        if self.status_conditions[Status.AGITATED] or self.status_conditions[Status.INJURED] or self.status_conditions[Status.VENGEFUL]:
            Damage = int(Damage * 1.2)

        return Damage


