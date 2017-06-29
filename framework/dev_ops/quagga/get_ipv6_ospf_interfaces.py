#!/usr/bin/env python

import re

def get_ipv6_ospf_interfaces(connection):
    command = 'vtysh -c "show ipv6 ospf6 interface"'
    output = connection.send_command(command)

    if output is None or 'failed' in output:
        return {
            'result': 'fail',
            'stdout': output
        }

    stdout = {}
    regexes = ['[^\s]+\sis\sup,\stype\s(?P<type>[^\n]+)',
        'inet6:\s(?P<inet6_addr>[^\n]+)',
        'Area\sID\s(?P<area>([0-9]{1,3}\.){3}[0-9]{1,3}),\sCost\s(?P<cost>[^\n]+)',
        'State\s(?P<state>[^,]+),\s.*,\sPriority\s(?P<priority>[^\n]+)',
        'Hello\s(?P<hello_time>[^,]+),\sDead\s(?P<dead_time>[^,]+),\sRetransmit\s(?P<retrans_time>[^\n])',
        'DR:\s(?P<dr>([0-9]{1,3}\.){3}[0-9]{1,3})\sBDR:\s(?P<bdr>([0-9]{1,3}\.){3}[0-9]{1,3})',
        'Detect\sMul:\s(?P<bfd_detect_multiplier>[^,]+),\sMin\sRx\sinterval:\s(?P<bfd_min_rx>[^,]+),\sMin\sTx\sinterval:\s(?P<bfd_min_tx>[^\n]+)'
    ]

    for line in output.splitlines():
        if ', type' in line:
            line = line.split()
            interface = line[0]
            stdout[interface] = {}
        else:
            for regex in regexes:
                match = re.search(regex, line)

                if match:
                    if 'inet6' in line:
                        cur_address = stdout[interface].get('inet6_addr')
                        stdout[interface]['inet6_addr'] = []

                        if cur_address is not None:
                            stdout[interface]['inet6_addr'].append(cur_address[0])

                        result = match.groupdict()
                        stdout[interface]['inet6_addr'].append(result['inet6_addr'])
                    else:
                        stdout[interface].update(match.groupdict())

    for interface in stdout:
        if not stdout[interface]:
            stdout[interface] = 'ospf6 is not running on this interface'

    return {
        'result': 'success',
        'stdout': stdout
    }
