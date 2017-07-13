#! /usr/bin/env python

import sys
import os
import subprocess

def edit_file(filename):
    editor = os.environ.get('EDITOR', 'vim')

    with open(filename, 'a') as edit_file:
        subprocess.call([editor, filename])
