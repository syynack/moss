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
        "bold": '\033[0;1m',
        "blue": '\033[0;36m'
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


def start_header(module_order):
    first_module = module_order[0]['module']
    print colour(' :: Modules to be executed: ', 'white', bold=True)

    for module in module_order:
        print colour('\t{}'.format(module['module']), 'white')

    print colour('\n :: First module: {}\n'.format(first_module), 'white', bold=True)


def module_start_header(task):
    print colour(' :: {}'.format(task), 'white'),


def module_end_header(result):
    if result == 'success':
        print colour(result, 'green', bold=True),
    else:
        print colour(result, 'red', bold=True),


def module_branch_header(next_step):
    print colour(' ( ', 'white') + colour('branch to {}'.format(next_step), 'magenta') + colour(' )', 'white'),


def module_focus_match_banner(next_module):
    if not next_module:
        print colour(' ( ', 'white') + colour('focus match', 'blue') + colour(' )', 'white'),
    else:
        print colour(' ( ', 'white') + colour('focus match branching to {}'.format(next_module), 'blue') + colour(' )', 'white'),


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


def print_data_in_json(data):
    print json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))


def write_json_to_file(data, filename):
    with open(filename, 'a+') as json_file:
        json_file.write(json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')))
