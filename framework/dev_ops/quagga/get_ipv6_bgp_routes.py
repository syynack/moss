#!/usr/bin/env python

import json

def get_ipv6_bgp_routes(connection):
    command = 'vtysh -c "show ipv6 route json"'
    output = connection.send_command(command)

    if output is None or 'failed' in output:
        return {
            'result': 'fail',
            'stdout': output
        }

    stdout = {}
    subroute_count = 0
    output = json.loads(output)

    for route in output:
        for subroute in output[route]:
            if output[route][subroute_count]['protocol'] == 'bgp':
                stdout[route] = output[route]

    return {
        'result': 'success',
        'stdout': stdout
    }
