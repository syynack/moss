#! /usr/bin/env python

import click

from moss.framework.management.ls import ls_cli_print_current_registered_modules

@click.command(short_help = 'List registered modules for all platforms')
def ls():
    ls_cli_print_current_registered_modules()
