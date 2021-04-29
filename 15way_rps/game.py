import random

from models import Player, RollType
from result_matrix import results


class RpsGame:
    GAME_NAME = '15-Way ROCK, PAPER & SCISSORS'

    def __init__(self, player1: Player, player2: Player):
        self.player1 = player1
        self.player2 = player2
        roll_types = list(RollType)
        self.rolls = [
            random.choice(roll_types),
            random.choice(roll_types),
            random.choice(roll_types),
            random.choice(roll_types),
            random.choice(roll_types),
        ]
        self._result = 0

    def _game_over(self):
        if self._result <= -3 or self._result >= 3:
            return True
        return False

    def start(self):
        count = 1

        while count <= 5:
            p2_roll = random.choice(self.rolls)
            p1_roll = RollType.from_choice(input(f'Choose your play:\n{RollType.valid_choices_str()} '))

            print(f'({self.player1}) {p1_roll} X {p2_roll} ({self.player2})')
            play_result = results[p1_roll][p2_roll]
            self._result += play_result
            print(f"Roll Result: {self._find_winner(play_result)}")
            print()

            if self._game_over():
                break

            count += 1

        self._declare_winner()

    def _find_winner(self, result):
        return f'{self.player1} Wins!' if result > 0 else f'{self.player2} Wins!' if result < 0 else 'Tie'

    def _declare_winner(self):
        print('-' * 50)
        winner = f"Result: {self._find_winner(self._result)}"
        print(f'{winner:>30}')
        print('-' * 50)

    @staticmethod
    def print_header() -> None:
        print('-' * 50)
        print(f'{RpsGame.GAME_NAME:>35}')
        print('-' * 50)
