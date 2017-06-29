#!/usr/bin/env python

import re

def get_interfaces_mac_address(connection):
    command = 'ifconfig'
    output = connection.send_command(command)

    if output is None or 'not found' in output:
        return {
            'result': 'fail',
            'stdout': output
        }

    stdout = []
    regex = '(?P<port_id>([^\s]+)).*?\sHWaddr\s(?P<ll_addr>([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2}))'

    for line in output.splitlines():
        data = re.search(regex, line)
        if data is not None:
            stdout.append(data.groupdict())

    return {
        'result': 'success',
        'stdout': stdout
    }
