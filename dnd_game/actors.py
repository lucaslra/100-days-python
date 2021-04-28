import random


class Creature:
    def __init__(self, name: str, level: int):
        self.name = name
        self.level = level

    def defensive_roll(self):
        roll = random.randint(1, 12)
        return roll * self.level

    def __eq__(self, other):
        return self.level == other.level

    def __lt__(self, other):
        return self.level < other.level

    def __le__(self, other):
        return self.level <= other.level

    def __ge__(self, other):
        return self.level >= other.level

    def __gt__(self, other):
        return self.level > other.level

    def __str__(self):
        return f'Level {self.level} {self.name}'

    def __repr__(self):
        return f'{type(self).__name__}(name={self.name}, level={self.level})'


class Dragon(Creature):
    def __init__(self, name: str, level: int, scaliness: int, breaths_fire: bool):
        super().__init__(name, level)
        self.scaliness = scaliness
        self.breaths_fire = breaths_fire

    def defensive_roll(self):
        roll = super().defensive_roll()
        roll = roll * self.scaliness
        if self.breaths_fire:
            roll = roll * 2

        return roll


class Wizard(Creature):
    def attack(self, creature: Creature):
        my_roll = self.defensive_roll()
        their_roll = creature.defensive_roll()

        return my_roll >= their_roll
