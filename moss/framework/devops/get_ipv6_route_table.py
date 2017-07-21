#!/usr/bin/env python

import re
from moss.framework.decorators import register

@register(platform = 'linux')
def linux_get_ipv6_route_table(connection):
    command = 'vtysh -c "show ipv6 route"'
    output = connection.send_command(command)

    if output is None or 'failed' in output:
        return {
            'result': 'fail',
            'stdout': output
        }

    stdout = {}
    route_regex = '^.{0,3}\s(?P<route>[^\s]+)'
    cost_regex = '\[(?P<admin_distance>.*)\/(?P<cost>.*)\]'
    via_regex = 'via\s(?P<via>[^,]+),\s(?P<egress_interface>[^,|\s]+)'

    output = output.splitlines()

    for index, line in enumerate(output):
        if line is None:
            del output[index]

    protocol_codes = {
        'K': 'kernel',
        'C': 'connected',
        'S': 'static',
        'R': 'ripng',
        'O': 'ospf6',
        'I': 'isis',
        'B': 'bgp',
        'T': 'table',
        'v': 'vnc',
        'V': 'vpn'
    }

    for line in output:
        route_match = re.search(route_regex, line)

        if route_match:
            route_match = route_match.groupdict()
            route = route_match['route']

            if route not in stdout:
                stdout[route] = {"nexthops": []}

            if 'C' not in line:
                cost_match = re.search(cost_regex, line)
                if cost_match:
                    cost_dict = cost_match.groupdict()
            else:
                cost_dict = {
                    "admin_distance": 0,
                    "cost": 0
                }

            if 'via' in line:
                via_match = re.search(via_regex, line)
                if via_match:
                    via_dict = via_match.groupdict()
            else:
                via_dict = {
                    "via": "directly connected",
                    "egress_interface": line.split()[-1]
                }

            stdout[route]["nexthops"].append({
                "protocol": protocol_codes[line[0]],
                "selected": False if line[1] == ' ' else True,
                "fib": False if line[2] == ' ' else True,
                "cost": cost_dict.get('cost'),
                "admin_distance": cost_dict.get('admin_distance'),
                "via": via_dict.get('via'),
                "egress_interface": via_dict.get('egress_interface')
            })

    return {
        'result': 'success',
        'stdout': stdout
    }
