#! /usr/bin/env python

import click

from moss.framework.management.init import init_cli_init_moss_working_directory


@click.command(short_help = 'Initialise a directory with base files')
def init():
    init_cli_init_moss_working_directory()
