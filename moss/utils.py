#! /usr/bin/env python

import struct
import fcntl
import termios
import time
import json


def colour(text, colour, bold=False):
    colours = {
        "white": '\033[0;97m',
        "green": '\033[0;92m',
        "red": '\033[0;31m',
        "magenta": '\033[0;35m',
        "reset": '\033[0;39m',
        "bold": '\033[0;1m'
    }

    if bold:
        return colours['bold'] + colours[colour] + text + colours['reset']
    else:
        return colours[colour] + text + colours['reset']


def get_terminal_width():
    h, w, _, _ = struct.unpack('HHHH', fcntl.ioctl(0, termios.TIOCGWINSZ, struct.pack('HHHH', 0, 0, 0, 0)))
    return int(w)


def start_banner():
    terminal_width = get_terminal_width()
    header = '[ Task Start ]'
    banner = '=' * ((terminal_width - len(header)) / 2) + header + '=' * ((terminal_width - len(header)) / 2)

    print colour(banner, 'white', bold=True)


def start_header(task):
    first_task = task['task_order'][0]['task_name']
    print colour(' :: Tasks to be executed: ', 'white', bold=True)

    for task in task['task_order']:
        print colour('\t{}'.format(task['task_name']), 'white')

    print colour('\n :: First task: {}\n'.format(first_task), 'white', bold=True)


def task_start_header(task):
    print colour(' :: {}'.format(task), 'white'),


def task_end_header(result):
    if result == 'success':
        print colour(result, 'green', bold=True),
    else:
        print colour(result, 'red', bold=True),


def task_branch_header(next_step):
    print colour(' ( ', 'white') + colour('branch to {}'.format(next_step), 'magenta') + colour(' )', 'white'),


def end_banner(result):
    terminal_width = get_terminal_width()
    header = header = '[ Task {} ]'.format(result)
    banner = '=' * ((terminal_width - len(header)) / 2) + header + '=' * ((terminal_width - len(header)) / 2)

    if result == 'success':
        print colour(banner + '\n', 'green', bold=True)
    else:
        print colour(banner + '\n', 'red', bold=True)


def timer():
    return time.time()


def runtime(start, end):
    return end - start


def pretty_print(data):
    print ''
    print json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
    print ''
