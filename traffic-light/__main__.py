import random
from itertools import cycle
from time import sleep

from rich.console import Console

colours = cycle(['green', 'yellow', 'red'])

console = Console(style='white')


def semaphore(color):
    light = f'|  [bold {color}]__[/bold {color}]  |\n' \
            f'| [bold {color}]|  |[/bold {color}] |\n' \
            f'|  [bold {color}]‾‾[/bold {color}]  |'
    off_color = 'white'
    off_light = f'|  [{off_color}]__[/{off_color}]  |\n' \
                f'| [{off_color}]|  |[/{off_color}] |\n' \
                f'|  [{off_color}]‾‾[/{off_color}]  |'

    semaph = f"{'-' * 8}\n" \
             f"{light if color == 'red' else off_light}\n" \
             f"{'-' * 8}\n" \
             f"{light if color == 'yellow' else off_light}\n" \
             f"{'-' * 8}\n" \
             f"{light if color == 'green' else off_light}\n" \
             f"{'-' * 8}"

    console.print(semaph, end='\r')
    print("\033[A" * 13)


try:
    for colour in colours:
        semaphore(colour)
        sleep(random.randint(3, 7))
except KeyboardInterrupt:
    exit(0)
