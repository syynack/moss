#!/usr/bin/env python

import re

def get_lldp_neighbors(connection):
    command = 'lldpctl -f xml'
    output = connection.send_command(command)

    if output is None or 'command not found' in output:
        return {
            'result': 'fail',
            'stdout': output
        }

    stdout = {}
    regexes = ['id\slabel.*"mac">(?P<remote_chassis_ll_addr>[^<]+)',
        'name\slabel.*"SysName">(?P<remote_hostname>[^<]+)',
        'id\slabel="PortID".*"mac">(?P<remote_port_ll_addr>[^<]+)',
        'descr\slabel="PortDescr">(?P<remote_port_id>[^<]+)'
    ]

    for line in output.splitlines():
        if 'interface label' in line:
            port_id = str(line.split()[2].split('=')[1].replace('"', ''))
            stdout[port_id] = {}

        for regex in regexes:
            match = re.search(regex, line)

            if match:
                stdout[port_id].update(match.groupdict())

    return {
        'result': 'success',
        'stdout': stdout
    }
