#!/usr/bin/env python

import json

def get_ipv6_route_table(connection):
    command = 'vtysh -c "show ipv6 route json"'
    output = connection.send_command(command)

    if output is None or 'failed' in output:
        return {
            'result': 'fail',
            'stdout': output
        }

    stdout = json.loads(output)

    return {
        'result': 'success',
        'stdout': stdout
    }
