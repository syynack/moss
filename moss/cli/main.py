#! /usr/bin/env python

import click
import init
import run
import ls


@click.group()
def main():
    pass


main.add_command(init.init, name = 'init')
main.add_command(run.run, name = 'run')
main.add_command(ls.ls, name = 'ls')
