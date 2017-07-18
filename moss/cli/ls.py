#! /usr/bin/env python

import click

from moss.register import REGISTER
from moss.utils import print_data_in_json


@click.command(short_help = 'List registered modules for all platforms')
def ls():
    print_register = {}

    for platform, funcs in REGISTER.iteritems():
        if not print_register.get(platform):
            print_register[platform] = []

        if isinstance(funcs, dict):
            for func_name, func in funcs.iteritems():
                print_register[platform].append(func_name)

    print_data_in_json(print_register)
