#! /usr/bin/env python

import click

from moss.register import registered_operations
from moss.utils import print_data_in_json


@click.command(short_help = 'List registered modules for all platforms')
def ls():
    print_register = {}

    for _type, item in registered_operations.iteritems():
        if not print_register.get(_type):
            print_register[_type] = {}

        for platform, func in item.iteritems():
            if not print_register[_type].get(platform):
                print_register[_type][platform] = []

            for func, module in func.iteritems():
                print_register[_type][platform].append(func)

    print_data_in_json(print_register)
