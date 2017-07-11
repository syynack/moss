#!/usr/bin/env python

import re

def linux_get_ipv6_ospf_neighbors_brief(connection):
    command = 'vtysh -c "show ipv6 ospf6 neighbor" | tail -n +2'
    output = connection.send_command(command)

    if 'failed' in output:
        return {
            'result': 'fail',
            'stdout': output
        }

    stdout = []
    regex = '(?P<neighbor_rid>([0-9]{1,3}\.){3}[0-9]{1,3})\s+' \
            '(?P<priority>[^\s]+)\s+' \
            '(?P<deadtime>[0-9]{2}:[0-9]{2}:[0-9]{2})\s+(?P<ospf_state>[^/]+)\/' \
            '(?P<ospf_interface_state>[^\s]+)\s+' \
            '(?P<uptime>[0-9]{2}:[0-9]{2}:[0-9]{2})\s' \
            '(?P<interface>[^\[]+)\[' \
            '(?P<interface_state>.*)]'

    for line in output.splitlines():
        match = re.match(regex, line, re.MULTILINE)

        if match:
            stdout.append(match.groupdict())

    return {
        'result': 'success',
        'stdout': stdout
    }
