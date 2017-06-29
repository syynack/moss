#!/usr/bin/env python

import json

def get_bgp_summary(connection):
    command = 'vtysh -c "show bgp summary json"'
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
