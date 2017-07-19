#! /usr/bin/env python

import click

from moss.cli import crypt
from moss.cli import init
from moss.cli import ls
from moss.cli import new
from moss.cli import run


@click.group()
def main():
    '''\b
                  ___  ________ _____ _____
                  |  \/  |  _  /  ___/  ___|
                  | .  . | | | \ `--.\ `--.
                  | |\/| | | | |`--. \`--. \ \b
                  | |  | \ \_/ /\__/ /\__/ /
                  \_|  |_/\___/\____/\____/

    Welcome to \033[1;32mmoss-ctrl\033[0m, the CLI tool for controlling MOSS.
    '''
    pass


main.add_command(crypt.crypt, name = 'crypt')
main.add_command(init.init, name = 'init')
main.add_command(ls.ls, name = 'list')
main.add_command(new.new, name = 'new')
main.add_command(run.run, name = 'run')
