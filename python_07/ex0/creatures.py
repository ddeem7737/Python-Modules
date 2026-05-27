from .creature import Creature, CreatureFactory

class Flameling(Creature):
    def __init__(self) -> None:
        super().__init__("Flameling", "Fire")
    
    def attack(self) -> str:
        return f"{self.name} uses Ember!"


class Pyrdon(Creature):
    def __init__(self) -> None:
        super().__init__("Pyrdon", "Fire/Flying")
    
    def attack(self) -> str:
        return f"{self.name} uses Flamethrower!"


class Aquabub(Creature):
    def __init__(self) -> None:
        super().__init__("Aquabub", "Water")
    
    def attack(self) -> str:
        return f"{self.name} uses Water Gun!"


class Torragon(Creature):
    def __init__(self) -> None:
        super().__init__("Torragon", "Water")
    
    def attack(self) -> str:
        return f"{self.name} uses Hydro Pump!"


class FlameFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Flameling()
    
    def create_evolved(self) -> Creature:
        return Pyrdon()


class AquaFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Aquabub()
    
    def create_evolved(self) -> Creature:
        return Torragon()