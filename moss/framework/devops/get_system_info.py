#!/usr/bin/env python

import re
from moss.framework.decorators import register

@register(platform = 'linux')
def linux_get_system_info(connection):
    '''
    Summary:
    Runs uname with optional flags to obtain detailed system information.

    Example expected output for uname -s -n -r -m -p -i -o:

    Linux d1-p1-l1-r1 4.4.0-31-generic x86_64 unknown unknown GNU/Linux

    Arguments:
    connection:         object, MossDeviceOrchestrator object

    Returns:
    dict

    Example:
    "stdout": {
        "architecture": "x86_64",
        "hardware_platform": "unknown",
        "hostname": "43085eb41a1e",
        "kernel_name": "Linux",
        "kernel_release": "4.9.27-moby",
        "operating_system": "GNU/Linux",
        "processor": "unknown"
    }
    '''

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
