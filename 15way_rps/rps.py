from game import RpsGame
from models import Player


def main():
    RpsGame.print_header()
    name = get_player_name()

    player1 = Player(name)
    player2 = Player('Computer')

    game = RpsGame(player1, player2)

    game.start()


def get_player_name() -> str:
    player_name = input('Player Name: ') or "Player 1"
    print(f'Welcome, {player_name}!')
    print()
    return player_name


if __name__ == '__main__':
    main()
