#!/usr/bin/env python

import re

def get_system_info(connection):
    command = 'uname -s -n -r -m -p -i -o'
    output = connection.send_command(command)

    if output is None or 'not found' in output:
        return {
            'result': 'fail',
            'stdout': output
        }

    output = output.split()

    stdout = {
        "kernel_name": output[0],
        "hostname": output[1],
        "kernel_release": output[2],
        "architecture": output[3],
        "processor": output[4],
        "hardware_platform": output[5],
        "operating_system": output[6]
    }

    return {
        'result': 'success',
        'stdout': stdout
    }
