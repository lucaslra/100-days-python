import argparse
import datetime
import time

import beepy


def check_valid_period(value):
    i_value = int(value)
    if i_value <= 0 or i_value > 1440:
        raise argparse.ArgumentTypeError(f'{value} is an invalid Pomodoro period. Choose between 0 and 1440')
    return i_value


parser = argparse.ArgumentParser(description='Pomodoro Timer')

command_parsers = parser.add_subparsers(title='commands', help='Pomodoro Commands', dest='command', required=True)

start_parser = command_parsers.add_parser('start', help='Start the work timer')
start_parser.add_argument('--minutes', '-m', help='Number of work minutes (default: 25)', type=check_valid_period,
                          default=25)
break_parser = command_parsers.add_parser('break', help='Start the break timer')
break_parser.add_argument('--long', '-l', action=argparse.BooleanOptionalAction,
                          help='Sets break to 10 minutes, instead of the standard 5')
break_parser.add_argument('--duration', '-d', type=check_valid_period,
                          help='Defines a custom duration for the break (default: 5)',
                          default=5)

args = parser.parse_args()


def as_timer(delta: datetime.timedelta):
    seconds = delta.seconds
    h = str(seconds // 60 // 60).rjust(2, '0')
    m = str(seconds // 60 % 60).rjust(2, '0')
    s = str(seconds % 60).rjust(2, '0')

    return f'{h}:{m}:{s}'


def new_timer(expected_duration):
    seconds = expected_duration * 60
    duration = datetime.timedelta(minutes=expected_duration)
    elapsed = datetime.timedelta(seconds=1)
    for _ in range(seconds):
        duration = duration - elapsed
        print(as_timer(duration), end='\r')
        time.sleep(1)
    beepy.beep(1)


def start_timer(minutes: int):
    print(f'Starting work timer')
    new_timer(expected_duration=minutes)
    print('Time for a break!')


def start_break(duration: int):
    print(f'Starting break timer')
    new_timer(expected_duration=duration)
    print('Time to get back to work!')


try:
    if args.command == 'start':
        start_timer(args.minutes)
    elif args.command == 'break':
        if args.long and args.duration == 5:
            args.duration = 10
        start_break(args.duration)
    else:
        raise ValueError(f'Invalid command: {command}')
except KeyboardInterrupt:
    print('Timer cancelled')
