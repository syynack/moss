#! /usr/bin/env python

import click

from moss.register import REGISTER
from moss.utils import colour

def _print_modules(data):
    if isinstance(data, dict):
        for key, item in data.iteritems():
            print colour(key, 'white')
            for module in data[key]:
                print '  {}'.format(module)
            print ''
    elif isinstance(data, list):
        for module in data:
            print module


def _get_registered_modules_for_platform(platform):
    for registered_platform in REGISTER:
        if registered_platform == platform:
            return REGISTER[registered_platform]


@click.command(short_help = 'List all currently registered modules')
def all():
    _print_modules(REGISTER)


@click.command(short_help = 'List all current registered Linux modules')
def linux():
    registered_linux_modules = _get_registered_modules_for_platform('linux')
    _print_modules(registered_linux_modules)


@click.group(short_help = 'List registered modules for a platform')
def ls():
    pass


ls.add_command(all, name = 'all')
ls.add_command(linux, name = 'linux')
