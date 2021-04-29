import enum


class RollType(enum.Enum):
    ROCK = 'Rock'
    PAPER = 'Paper'
    SCISSORS = 'Scissors'
    GUN = 'Gun'
    LIGHTNING = 'Lightning'
    DEVIL = 'Devil'
    DRAGON = 'Dragon'
    WATER = 'Water'
    AIR = 'Air'
    SPONGE = 'Sponge'
    WOLF = 'Wolf'
    TREE = 'Tree'
    HUMAN = 'Human'
    SNAKE = 'Snake'
    FIRE = 'Fire'

    @staticmethod
    def valid_choices_str():
        return '''* [R]ock            * [G]un             * [L]ightning
* [D]evil           * [Dr]agon          * [W]ater
* [A]ir             * [P]aper           * [Sp]onge
* [Wo]lf            * [T]ree            * [H]uman
* [Sn]ake           * [S]cissors        * [F]ire
---
'''

    @staticmethod
    def from_choice(choice: str):
        choice = choice.lower()
        if choice == 'r':
            return RollType.ROCK
        elif choice == 'p':
            return RollType.PAPER
        elif choice == 's':
            return RollType.SCISSORS
        elif choice == 'g':
            return RollType.GUN
        elif choice == 'l':
            return RollType.LIGHTNING
        elif choice == 'd':
            return RollType.DEVIL
        elif choice == 'dr':
            return RollType.DRAGON
        elif choice == 'w':
            return RollType.WATER
        elif choice == 'a':
            return RollType.AIR
        elif choice == 'sp':
            return RollType.SPONGE
        elif choice == 'wo':
            return RollType.WOLF
        elif choice == 't':
            return RollType.TREE
        elif choice == 'h':
            return RollType.HUMAN
        elif choice == 'sn':
            return RollType.SNAKE
        elif choice == 'f':
            return RollType.FIRE
        else:
            raise ValueError(f'Invalid choice. Valid roll choices are:\n{RollType.valid_choices_str()}')

    def __str__(self):
        return self.value


class Player:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __format__(self, format_spec):
        return f'{self.name:{format_spec}}'

    def __repr__(self):
        return f"{type(self).__name__}(name='{self.name}')"
