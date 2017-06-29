#!/usr/bin/env python

import re

def get_interfaces_statistics(connection):
    command = 'ifconfig -a'
    output = connection.send_command(command)

    if output is None or 'command not found' in output:
        return {
            'result': 'fail',
            'stdout': output
        }

    stdout = {}
    regexes = ['Link encap:(?P<link_encapsulation>[^\s]+)',
        'MTU:(?P<mtu>[^\s]+)',
        'RX\spackets:(?P<rx_ok>[^\s]+)\serrors:(?P<rx_err>[^\s]+)\sdropped:(?P<rx_drp>[^\s]+)\soverruns:(?P<rx_ovr>[^\s]+)\sframe:(?P<rx_frm>[^\s]+)',
        'TX\spackets:(?P<tx_ok>[^\s]+)\serrors:(?P<tx_err>[^\s]+)\sdropped:(?P<tx_drp>[^\s]+)\soverruns:(?P<tx_ovr>[^\s]+)\scarrier:(?P<tx_car>[^\s]+)',
        'collisions:(?P<collisions>[^\s]+)\stxqueuelen:(?P<tx_queue_length>[^\s]+)',
        'RX\sbytes:(?P<rx_bytes>[^\s]+)\s\(((?P<rx_total>[^)]+))\)',
        'TX\sbytes:(?P<tx_bytes>[^\s]+)\s\(((?P<tx_total>[^)]+))\)'
    ]

    for line in output.splitlines():

        if 'Link encap' in line:
            split_line = line.split()
            port_id = split_line[0]
            stdout[port_id] = {}

        for regex in regexes:
            match = re.search(regex, line)

            if match:
                stdout[port_id].update(match.groupdict())

    return {
        'result': 'success',
        'stdout': stdout
    }
