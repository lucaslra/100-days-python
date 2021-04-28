import enum


class RollType(enum.Enum):
    ROCK = 'Rock'
    PAPER = 'Paper'
    SCISSORS = 'Scissors'

    @staticmethod
    def from_choice(choice: str):
        choice = choice.lower()
        if choice == 'r':
            return RollType.ROCK
        elif choice == 'p':
            return RollType.PAPER
        elif choice == 's':
            return RollType.SCISSORS
        else:
            raise ValueError('Invalid choice. Valid roll choices are [R]ock, [P]aper or [S]cissors')

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
