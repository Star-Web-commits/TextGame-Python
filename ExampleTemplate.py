class Character:
    def __init__(self, name, health, attack, heal, status):
        self.name = name
        self.health = health
        self.attack = attack
        self.heal = heal
        self.status = status

def display_battle(players, monster):
    # Calculate the width of the columns dynamically
    max_name_len = max(len(c.name) for c in players + [monster])
    max_health_len = max(len(str(c.health)) for c in players + [monster])
    max_attack_len = max(len(str(c.attack)) for c in players + [monster])
    max_heal_len = max(len(str(c.heal)) for c in players + [monster])
    max_status_len = max(len(c.status) for c in players + [monster])

    # Set minimum column widths
    name_width = max(15, max_name_len)
    health_width = max(6, max_health_len)
    attack_width = max(6, max_attack_len)
    heal_width = max(4, max_heal_len)
    status_width = max(20, max_status_len)

    # Header
    print("=" * (name_width + health_width + attack_width + heal_width + status_width + 16))
    print(f"| {'PLAYERS'.center(name_width + health_width + attack_width + heal_width + status_width + 7)}      |")
    print("=" * (name_width + health_width + attack_width + heal_width + status_width + 16))

    for player in players:
        name = player.name.ljust(name_width)
        health = str(player.health).rjust(health_width)
        attack = str(player.attack).rjust(attack_width)
        heal = str(player.heal).rjust(heal_width)
        status = player.status.ljust(status_width)
        print(f"| {name} | {health} | {attack} | {heal} | {status} |")
    
    print("=" * (name_width + health_width + attack_width + heal_width + status_width + 16))
    print(f"| {'MONSTER'.center(name_width + health_width + attack_width + heal_width + status_width + 7)}      |")
    print("=" * (name_width + health_width + attack_width + heal_width + status_width + 16))

    name = monster.name.ljust(name_width)
    health = str(monster.health).rjust(health_width)
    attack = str(monster.attack).rjust(attack_width)
    heal = str(monster.heal).rjust(heal_width)
    status = monster.status.ljust(status_width)
    print(f"| {name} | {health} | {attack} | {heal} | {status} |")
    print("=" * (name_width + health_width + attack_width + heal_width + status_width + 16))

# Example usage
players = [
    Character("Warrior", 100, 20, 10, "Healthy"),
    Character("Mage", 80, 25, 8, "Injured")
]

monster = Character("Dragon", 500, 50, 0, "Flying")

display_battle(players, monster)
