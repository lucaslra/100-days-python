import random

from actors import Creature, Wizard, Dragon

GAME_TITLE = 'WIZARD GAME'


def main():
    print_header()
    game_loop()


def print_header():
    print('-' * 30)
    print(f'{GAME_TITLE:>20}')
    print('-' * 30)


def game_loop():
    creatures = [
        Creature('Bat', 5),
        Creature('Toad', 1),
        Creature('Tiger', 12),
        Dragon('Red Dragon', 50, 10, True),
        Wizard('Evil Wizard', 1000),
    ]

    print(creatures)

    hero = Wizard('Gandolf', 75)
    while True:
        active_creature = random.choice(creatures)

        print(f'A {active_creature.name} of level {active_creature.level} has appear from a dark and foggy forest...')
        print()

        cmd = input('Do you [a]ttack, [r]unaway, or [l]ook around? ').lower()

        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
                print(f'The Wizard defeated {active_creature.name}')
            else:
                print(f'The Wizard has been defeated by the powerfull {active_creature.name}')
        elif cmd == 'r':
            print('The wizard has become unsure of his power and flees!!!')
        elif cmd == 'l':
            print(f'The wizard {hero.name} takes in the surroundings and sees:')
            for c in sorted(creatures):
                print(f'* {c.name} of level {c.level}')
        else:
            print('OK, exiting the game... bye!')
            break

        if not creatures:
            print("You've defeated all the creatures, well done!")
            break

        print()


if __name__ == '__main__':
    main()
