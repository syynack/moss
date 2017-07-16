#!/usr/bin/env python

import re

def linux_get_ipv6_ospf_neighbors_detail(connection):
    command = 'vtysh -c "show ipv6 ospf6 neighbor detail"'
    output = connection.send_command(command)

    if 'failed' in output:
        return {
            'result': 'fail',
            'stdout': output
        }

    stdout = {}
    regexes = ['Area\s(?P<area>[^\s]+)',
        'Link-local\saddress:\s(?P<inet6_link_local_addr>[^\s]+)',
        'State\s(?P<state>[^\s]+)\sfor\sa\sduration\sof\s(?P<uptime>[^\s]+)',
        'BDR\s(?P<remote_dr>([0-9]{1,3}\.){3}[0-9]{1,3})',
        '\/(?P<remote_bdr>([0-9]{1,3}\.){3}[0-9]{1,3})',
        ',\sPriority\s(?P<priority>[^\s]+)',
        'BFD:\sType:\s(?P<bfd_type>[^\n]+)',
        'Detect\sMul:\s(?P<bfd_detect_multiplier>[^,]+),\sMin\sRx\sinterval:\s(?P<bfd_min_rx>[^,]+),\sMin\sTx\sinterval:\s(?P<bfd_min_tx>[^\n]+)'
    ]

    for line in output.splitlines():
        if 'Neighbor' in line:
            line = line.split()
            neighbor, interface = line[1].split('%')
            stdout[neighbor] = {}
        else:
            for regex in regexes:
                match = re.search(regex, line)

                if match:
                    stdout[neighbor].update(match.groupdict())
                    stdout[neighbor].update({'interface': interface})

    return {
        'result': 'success',
        'stdout': stdout
    }
